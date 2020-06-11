class Foo(object):
    def __init__(self):
        self.__a = 1

    def __test_method(self):
        return "Hello"

    @classmethod
    def testXX(cls):
        return "xxx"

f = Foo()
print(f._Foo__a)
print(f._Foo__test_method)
print(Foo.testXX())