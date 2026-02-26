# Skilltree
本模块用于解析`scripts/prefabs/`中的技能树定义数据并生成json格式文件。

后续需要手动上传到维基`Module:Skilltree`的对应子模块中。


## 使用

1. 按照根目录下的README.md中的步骤配置好环境、账号信息和游戏目录。
2. 在根目录下执行`Skilltree/run.py`文件

正常情况下输出类似于:

```log
...
INFO:__main__:Processing skilltree for character: wathgrithr
INFO:__main__:skilltree for character: wathgrithr saved to /home/hikaru/python-projects/dontstarve-huijiwiki-scripts/Skilltree/skilltrees/skilltree_wathgrithr.json
INFO:__main__:Processing skilltree for character: wormwood
INFO:__main__:skilltree for character: wormwood saved to /home/hikaru/python-projects/dontstarve-huijiwiki-scripts/Skilltree/skilltrees/skilltree_wormwood.json
INFO:__main__:Processing skilltree for character: wilson
INFO:__main__:skilltree for character: wilson saved to /home/hikaru/python-projects/dontstarve-huijiwiki-scripts/Skilltree/skilltrees/skilltree_wilson.json
...
```

3. 之后将`Skilltree/skilltrees/`目录下的文件内容复制粘贴到维基`Module:Skilltree`的对应子模块的`"defs"`键中。
`"metainfo"`键中的信息仍需要手动填写。
(对绝大多数角色来说，`"metainfo"`键中的数据除了背景图外都可以直接复制粘贴。当后续角色技能树完善后，这部分会提供更好的实现方式以方便自动上传。)

## 反馈
使用过程中遇到问题或有建议，你可以:
1. 在[GitHub仓库](https://github.com/HarryS561/dontstarve-huijiwiki-scripts/issues)的Issues中反馈。
2. 维基编辑QQ群里联系2199。