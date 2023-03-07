class Person():
    population=50
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @classmethod
    def get_population(cls):
        return cls.population
    
    @staticmethod
    def is_adult(age):
        return age>=18
    
    def display(self):
        print(f"{self.name} is {self.age} years old")
    
a=Person("bill",18)
print(Person.get_population()) # can be called without generate a new object
print(Person.is_adult(5))