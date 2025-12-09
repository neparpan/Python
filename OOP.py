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

"""
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




