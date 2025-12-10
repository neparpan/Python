# class and object
#class is blueprint for creating objects

"""
class Student:
    name ="arpan"


s1 = Student()#object
print(s1.name)



class Car:
    color ="black"
    brand = "bmw"


car1 = Car()
print(car1.color)
print(car1.brand)



#constructor
# __init__ function


class Student:
    
    def __init__(self, name, marks):
       # print(self)
       self.name = name
       self.marks = marks
print("creating new student in database")
        
s1 = Student("karan",91)
print(s1.name, s1.marks)


s2 = Student("bishal", 90)
print(s2.name, s2.marks)




#class and instance attributes
# Class.attr 
# obj.attr 


class Student:
    college_name = "ABC College"
    name = "anonymous" #class attr


    def __init__(self, name , marks):
        self.name = name #obj attr > class attr
        self.marks = marks
        print("adding new student in Database..")

S1 = Student("karan", 99)
print(S1.name)         



#Methods
#methods are functions that belong to object

class Student:
    college_name = "xyz college"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student")

    
    def get_marks(self):
        return self.marks


s1 = Student("arpan", 98)
s1.welcome()
print(s1.get_marks())
        






# Static methods
# methods that don't use the self parameter (work at class level)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum= 0
        for val in self.marks:
            sum += val
            print("hi", self.name, "your avg score is:", sum/3)


s1 = Student("tony stark", [99,98,97])
s1.get_avg()
s1.hello()
        

# Abstration 
#hiding the implementation details of a class and only showing the essential features to the user



#Encapsulation
#Wrapping data and functions into a single unit(object)

# Abstration 


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")


car1 = Car()
car1.start()






#del keyword

class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("arpan")
print(s1.name) 
del s1.name



#private attributes and method
#  __ for private

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no =acc_no
        self.__acc_pass = acc_pass


    def reset_pass(self):
        print(self.__acc_pass)


acc1 = Account("123345", "abcdef")

print(acc1.acc_no)
print(acc1.reset_pass())




#print annonymous

class Person:
    __name = "anonymous"


    def __hello(self):
     print("hello person!!")


    def welcome(self):
      self.__hello()

p1 = Person()
print(p1.welcome())


 

#Inheritance
#clas car:
#...........


# class TOYOTAcAR(car):
#.......

class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name



car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")


car1.start()  
car2.stop()  


# multi level inheritance

class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand



class Fortuner(Car):
    def __init__(self, type):
        self.type =type
        

Car1 = Fortuner("diesel")
Car1.start()



#multiple Inheritance

class A :
    varA = "welcome to class A"

class B :
    varB = "welcome to class B"


class C(A, B) :
    varC = "welcome to class C"


c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)



#super method
# used to accss methods of the parent class

class Car:
    def __init__(self, type):
        self.type = type

        @staticmethod
        def start():
            print("car started..")


        @staticmethod
        def stop():
            print("car stopped")

class ToyotaCar(Car):
    def __init__(self, name, type):
          self.name = name
          super().__init__(type)

car1 = ToyotaCar("Supra", "petrol")
print(car1.type)





# Class Method
# a class method is bound to the class & receives the class as an implicit first argument.
#note: static method can't access or modify class state & generally for utility


class Person:
    name= "anonymous"

    #def changeName(self, name):
        #self.name = name
        #self.__class__.name = "arpan"

#class method

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("arpan nepal")
print(p1.name)




#property method


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)  

stu1.phy = 86
print(stu1. percentage)

 """

# Polymorphism : operator overloading
#when the same operator is allowed to have different meaning to use the method as a property


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img


    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def add(self, num2):
        newReal = self.real +num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()


num2 = Complex(4, 6)
num2.showNumber()


num3 = num1.add(num2)
num3.showNumber()