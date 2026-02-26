from tools.dummy import DummyTable
from .skilltree import SKILL_TREE_FNS
from .serialize import SkillTreeEncoder

DST_GLOBALS = {
    "STRINGS": DummyTable("STRINGS"),
    "SPELLTYPES": DummyTable("SPELLTYPES"),
    "UPGRADETYPES": DummyTable("UPGRADETYPES"),
    "TUNING": DummyTable("TUNING"),
}

__all__ = ["DST_GLOBALS", "SKILL_TREE_FNS", "SkillTreeEncoder"]
