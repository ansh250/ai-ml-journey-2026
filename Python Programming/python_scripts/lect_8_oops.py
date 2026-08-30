'''
     #OOPS Concepts in python
class Student:
    college_name = "PSIT" #for students college name is same so we do not need to make it inside the consstructor.
    # default constructor
    def __init__(self):
        pass
    # parameterized constructor
    def __init__(self,name,marks):
        self.name = name    # these are called attributes of the class like here name and class
        self.marks = marks
        print("Instance created in database")
        # methods
    def welcome(self):
        print("Welcome to the ",self.college_name,":",self.name)
    # static method
    @staticmethod    #decorator which is used when we want to create a fun without self    
    def hello():
        print("Hello")
s1 = Student("Karan dayal",90) # at the time of instace creation when we pass our values to the constructor 
                               # so which constructor match our parameters that is calledautomatically
#print(s1)
print(s1.name,s1.marks)
print(s1.college_name)
s1.welcome()
s1.hello()

# Program based on OOPs
class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def Average(self):
        return (self.marks1+self.marks2+self.marks3)//3
s1 = Student("Mr Beast",40,50,100)
print(s1.name,s1.marks1,s1.marks2,s1.marks3)
print(s1.Average())


# Abstraction Example
class Car:
    def __init__(self):
        self.clutch = False
        self.brk = False
        self.accelerate = False
    def start(self):
        self.clutch = True
        self.accelerate = True
        print("Car Started")
c1 = Car()
c1.start()    
'''
# Account class example
class Account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no
    def debit(self,amount):
        if(amount>self.balance):
            print("Insufficient Balance")
            return
        self.balance = self.balance - amount
        print("Amount Debitted rest of the balance is : ",self.balance)
    def credit(self,amount):
        self.balance = self.balance+amount
        print("Amount Creditted Sucessfully balnce is : ",self.balance)
a1 = Account(1000,123)
a1.debit(500)
a1.credit(5000)
a1.credit(888)
a1.debit(70000)