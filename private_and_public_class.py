class Test():
    def __init__(self):
        self.__data=[]
    def add(self,item):
        self.__data.append(item)
    def printdata(self):
        print(self.__data)
        # only object in this class can read this, for others\
        # none object, can only read them through _Test__data
    def __say(self):
        return self.__data
class Test(Test):
    def func(self):
        print(self.__data)

a=Test()
a.add("123")
print(a._Test__data) #call private attribute
a.printdata()
print(f"say result:{a._Test__say()}")#call private function
print(a.__dict__)# call all attributes in a
# print(dir(a))# call all attributes and functions in a
a.func()# when father and son class have same name, then can call private attribute 
    