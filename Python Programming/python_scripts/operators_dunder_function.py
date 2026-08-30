#operators_dunder_function.py
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def show(self):
        print(self.real, 'i +' , self.img ,'j')
    def __add__(self,num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img   
        return Complex(new_real,new_img)
        '''
    def add(self,num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img        if we not use dunder function
        return Complex(new_real,new_img)
        '''
num1 = Complex(1,3)
num2 = Complex(4,5)
num1.show()
num2.show()
 #  num3 = num1.add(num2)   when not using dunder function
num3 = num1+num2
num3.show()