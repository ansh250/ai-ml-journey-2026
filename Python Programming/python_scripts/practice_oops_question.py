# define a circle class to create a circle class with radius r using the constructor and develop the method area and peremeter.
'''
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def Area(self):
        return 22/7 * self.radius * self.radius
    def Peremeter(self):
        return 2*22/7*self.radius
c1 = Circle(21)
print(c1.radius)
print(c1.Area())
print(c1.Peremeter())
'''
# definr a employe class with attributes role,department & salary and make a shoedetails method.
'''
class Employe:
    def __init__(self,role,department,salary):
        self.role = role
        self.department  = department
        self.salary = salary
    def showdetails(self):
        print("Employe Role is: ",self.role)
        print("Employe Department is: ",self.department)
        print("Employe Salary is: ",self.salary)
class Engineer(Employe):
    def __init__(self,name,age,role,department,salary):
        self.name = name
        self.age = age
        super().__init__(role,department,salary)

e1 = Employe("Software Engineer","CSE",98000)
e1.showdetails()
en1 = Engineer("Mohit",27,"Senior Engineer","IOT","150000")
print("Name : ",en1.name)
print("Age : ",en1.age)
en1.showdetails()
'''
# Create a class order which stores item and its price use dunder (__gt__)function to convey
# that order1 > order2 if price of order1 > price of order 2
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,o2):
        return self.price>o2.price
o1 = Order("Finger Chips",99)
print(o1.item,o1.price)
o2 = Order("Pizza",199)
print(o2.item,o2.price)
print(o1>o2)
print(o2>o1)
