"""为skilltree相关lua文件解析而构造的一些函数"""

from lua_core.lua_modules import ModuleWrapper
from lua_core.lua_types import LuaTable
from tools.dummy import DummyTable


class SkillTreeFns:
    @staticmethod
    def CountSkills(*args):
        return

    @staticmethod
    def HasTag(*args):
        return

    @staticmethod
    def CountTags(*args):
        return

    @staticmethod
    def SkillHasTags(*args):
        return

    @staticmethod
    def MakeFuelWeaverLock(extra_data=None, not_root=None):
        lock = LuaTable(
            desc=DummyTable("STRINGS").SKILLTREE.ALLEGIANCE_LOCK_2_DESC,
            root=not not_root,
            group="allegiance",
            tags=LuaTable(enumerate(("allegiance", "lock"))),
            lock_open=True,
        )

        if extra_data is not None:
            lock.pos = extra_data.pos
            lock.connects = extra_data.connects
            lock.group = extra_data.group or lock.group
        return lock

    @staticmethod
    def MakeNoShadowLock(extra_data=None, not_root=None):
        lock = LuaTable(
            desc=DummyTable("STRINGS").SKILLTREE.ALLEGIANCE_LOCK_5_DESC,
            root=not not_root,
            group="allegiance",
            tags=LuaTable(enumerate(("allegiance", "lock"))),
            lock_open=True,
        )

        if extra_data is not None:
            lock.pos = extra_data.pos
            lock.connects = extra_data.connects
            lock.group = extra_data.group or lock.group
        return lock

    @staticmethod
    def MakeCelestialChampionLock(extra_data=None, not_root=None):
        lock = LuaTable(
            desc=DummyTable("STRINGS").SKILLTREE.ALLEGIANCE_LOCK_3_DESC,
            root=not not_root,
            group="allegiance",
            tags=LuaTable(enumerate(("allegiance", "lock"))),
            lock_open=True,
        )

        if extra_data is not None:
            lock.pos = extra_data.pos
            lock.connects = extra_data.connects
            lock.group = extra_data.group or lock.group
        return lock

    @staticmethod
    def MakeNoLunarLock(extra_data=None, not_root=None):
        lock = LuaTable(
            desc=DummyTable("STRINGS").SKILLTREE.ALLEGIANCE_LOCK_4_DESC,
            root=not not_root,
            group="allegiance",
            tags=LuaTable(enumerate(("allegiance", "lock"))),
            lock_open=True,
        )

        if extra_data is not None:
            lock.pos = extra_data.pos
            lock.connects = extra_data.connects
            lock.group = extra_data.group or lock.group
        return lock

    @staticmethod
    def MakePurelyVisualLock(*args):
        return


SKILL_TREE_FNS = ModuleWrapper(SkillTreeFns)
