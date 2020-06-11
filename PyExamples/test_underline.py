def func_1():
    print("func_1")

def _func_2():
    print("_func_2")

def __func_3():
    print("__func_3")


class test_underlineA():

    a1 = 'a1'
    _a1 = '_a1'
    __a1 = '__a1'

    def __init__(self):
        self.c1 = 'c1'
        self._c1 = '_c1'
        self.__c1 = '__c1'
        print("here")

    def _test_a(self):
        print("_test_a")

    def __test_a(self):
        print("__test_a")

class Test(object):
    def name(self):
        self.__nam = "hhh"

    def __nume(self):
        print("666")


class test_underlineB(test_underlineA):

    def print_(self):
        print("print:")
        print("a1:"+self.a1)
        print("_a1:" + self._a1)
        print("__a1:" + self.__a1)
        self._test_a()
        self.__test_a()

class testC(test_underlineA):
    def print_(self):
        print("testC")

test = Test()
test._Test__nume()
test_underlineA.a1 = 'b'
test_underlineA.b1 = 'b1'
test2 = test_underlineB()
print(test2.a1)
print(test2.b1)
test2.d1 = 'd1'
del test_underlineA.b1
#print(test_underlineA.b1)
print(test2._c1)
print(test2._test_underlineA__c1)


#print(test_underlineB._a1)
#test_underlineB._test_a()


"""
testB = test_underlineB()
test_underlineC.print_()
print(test_underlineB.a1)
print(test_underlineB._a1)
print(testB.a1)
print(testB._a1)
#print(testB.__a1)
testB._test_a()
#testB.__test_a()
testB.print_()
"""

