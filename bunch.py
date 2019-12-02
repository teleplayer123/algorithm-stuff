class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self

tree= Bunch
t = tree(left=tree(left="a", right="b"), right=tree(left="c"))
print(t["left"])

class bunch(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self

def unbunchifiy(x):
    if isinstance(x, dict):
        return dict((k, v) for k, v in x.items())