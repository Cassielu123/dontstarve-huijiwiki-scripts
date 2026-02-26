from luaparser import ast

import json
import zipfile
import os
import logging
import importlib
import sys
from contextlib import redirect_stdout

from parser import LuaParser, Scope
from lua_core import LUA_BUILTINS
from dst_core import (
    DST_GLOBALS,
    SKILL_TREE_FNS,
    SkillTreeEncoder,
)
import constants

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
client = importlib.import_module("main").site

# 配置日志为INFO级别
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_img_url(filename):
    """
    获取图片的url
    """
    result = client.api(
        "query",
        titles=f"File:{filename}",
        prop="imageinfo",
        iiprop="url",
        format="json",
    )
    pages = result["query"]["pages"]
    page = list(pages.values())[0]
    if "imageinfo" not in page:
        return None
    return page["imageinfo"][0]["url"]


def main():
    img_url_mapping = {}
    with zipfile.ZipFile(constants.SCRIPTS_PATH) as zip_ref:
        for file_info in zip_ref.infolist():
            # 检查文件是否在目标目录中
            filename = file_info.filename
            if filename.startswith("scripts/prefabs/skilltree_w"):
                character = filename.split("_")[-1].split(".")[0]
                logger.info(
                    "Processing skilltree for character: %s", character
                )
                with zip_ref.open(filename) as f_read:
                    content = f_read.read().decode("utf-8")
                    with open(os.devnull, "w") as f_write:
                        with redirect_stdout(f_write):
                            chunk = ast.parse(content)
                parser = LuaParser(builtins=LUA_BUILTINS)
                parser.scope.top_scope.update(DST_GLOBALS)
                parser.scope.top_scope.update(SkillTreeFns=SKILL_TREE_FNS)
                parser.visit(chunk)
                fn = parser.globals["BuildSkillsData"]
                with Scope(parser, fn.scope, enclosure=True):
                    parser.visit(fn.body)
                    res = parser.return_value
                skilltree_json_path = os.path.join(
                    constants.SKILLTREE_OUTPUT_DIR,
                    f"skilltree_{character}.json",
                )
                if not os.path.exists(constants.SKILLTREE_OUTPUT_DIR):
                    os.makedirs(constants.SKILLTREE_OUTPUT_DIR)
                skilltree_def = res["SKILLS"]
                for skill_def in skilltree_def.values():
                    if "icon" in skill_def:
                        icon_name = skill_def["icon"]
                        if icon_name not in img_url_mapping:
                            img_url = get_img_url(f"{icon_name}.png")
                            if img_url is None:
                                logger.warning("%s's url not found", icon_name)
                                continue
                            img_url_mapping[icon_name] = img_url
                        else:
                            img_url = img_url_mapping[icon_name]
                        skill_def["icon_url"] = img_url
                with open(skilltree_json_path, "w") as f:
                    json.dump(
                        skilltree_def,
                        f,
                        cls=SkillTreeEncoder,
                        indent=4,
                        ensure_ascii=False,
                    )
                logger.info(
                    "skilltree for character: %s saved to %s",
                    character,
                    skilltree_json_path,
                )


if __name__ == "__main__":
    main()
