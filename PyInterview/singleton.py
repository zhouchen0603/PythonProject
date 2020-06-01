class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self, name):
        self.name = name

class Nana(Singleton):
    def __init__(self, name):
        self.name = name

a = MyClass("HelloA")
print(a.name)
b = MyClass("HelloB")
print(a.name)
print(b.name)
b.name = "HelloC"
print(a.name)
print(b.name)
