class Person:
    def __init__(self):
        print("init")
        # self.name=name
        # self.age=age
    def __new__(cls):
        print("new")
        return super().__new__(cls)
    def __del__(self):
        # print("delete this instance")
        pass
    def __str__(self):
        return type(self).__name__
    def __repr__(self):
        return "<Person class>"
    def __bytes__(self):
        return b"bytes"
    def __call__(self):
        print("call function")
        
### new method
a1=Person()
# run new first then run init

### del method
# del a1

### str method
print(a1)
print(type(a1))

### repr method
print(a1.__repr__)
print(repr("abc"))

### bytes
print(bytes(a1))

### call
print(a1())

###hasstr
print(hasattr(a1,"name"))
a1.name="abc"
print(hasattr(a1,"name"))
'''
False
True
'''

###getattr
print(getattr(a1,"name"))
'''
abc
'''

###setattr
setattr(a1,"subname","dabendan")
print(a1.subname)
'''
dabendan
'''

###delattr
delattr(a1,"subname")
a1.subname
    
    