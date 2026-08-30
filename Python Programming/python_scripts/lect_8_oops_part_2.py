# del keyword
'''
class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("ansh")
print(s1.name)
del(s1.name)
print(s1.name)
'''
# For making the methods and attribute  private we use __ to make them safe conceptually
'''
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
a1 = Account(1234,"abcd")
print(a1.acc_no)
print(a1.__acc_pass)
'''
# Inheritance
'''
class Car:
    @staticmethod
    def start():
        print("Engine Started")
    @staticmethod
    def stop():
        print("Engine Off")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
v1 = ToyotaCar("Fortuner")
print(v1.name)
v1.start()
v1.stop()
'''
# super method 
'''
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("Engine Started")
    @staticmethod
    def stop():
        print("Engine Off")
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
v1 = ToyotaCar("Fortuner","Petrol")
print(v1.type)
v1.start()
print(v1.name)
v1.stop()
'''
# class method or decorator
'''
class Person:
    name = "anonyomous"
    
    @classmethod
    def changename(cls,name):
        cls.name = name
        #other method to change class attributes
        # 1. Person.name = name directly use this
        # 2. self.__class__.name = "Rahul"  directly using this function 
p1 = Person()
print(p1.name)
p1.changename("Rahul kumar")
print(p1.name)
print(Person.name)
'''
# property decorator
class Marks:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
m1 = Marks(98,65,97)
print(m1.percentage)
m1.chem = 99
print(m1.percentage)