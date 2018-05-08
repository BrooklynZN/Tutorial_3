#Answer to Question 1
import numpy

class Complex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
        #Calculating Absolute value
    def abs(self):
        y=np.sqrt(self.r**2+self.i**2)
        rertun y
        #Subtraction
    def subt(self,x):
        real1 = self.r - x.r
        im1 = self.i - x.i
        return Complex(real1,im1)
        #Addition
    def addn(self,y):
        real2 = self.r + y.r
        im2 = self.i +  y.i
        return Complex(real2,im2)
        #Multiplication 
    def multi(self,z):
        real3 = (self.r*z.r)-(self.i*z.i)
        im3 = (self.r*z.i)+(z.r*self.i)
        return Complex(real3,im3)
        #Division
    def div(self,d):
        real4 = ((self.r*d.r)+(self.i*d.i))/(d.r**2+d.i**2)
        im4 = ((self.i*d.r)-(self.r*d.i))/(d.r**2+d.i**2)
        return Complex(real4,im4)