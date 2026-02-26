class DummyTable:
    # 用于模拟未定义的Lua Table
    def __init__(self, name, parent=None):
        self.table = dict()
        self.name = name
        self.parent = parent

    # 支持嵌套访问, 访问键总是返回DummyTable
    def __getitem__(self, key):
        if key not in self.table:
            self.table[key] = DummyTable(key, self)
        return self.table[key]

    # 访问属性时如果属性不存在则访问__getitem__
    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        return self[key]

    def __setattr__(self, name, value):
        if name in ["table", "name", "parent"]:
            super().__setattr__(name, value)
        else:
            self.table[name] = value

    def __add__(self, other):
        if type(other) is str:
            return self.__str__() + other

    def __str__(self):
        s = self.name
        if self.parent:
            s = f"{self.parent}.{s}"
        return s

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        s = str(self)
        if s.startswith("STRINGS."):
            from read_po import scan_chn_po

            return scan_chn_po()[s]["msgstr"]
        return self.__str__()
