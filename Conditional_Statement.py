# we will be using if-elif-else
"""
Light = "green"

if(Light== "red"):     # if will always check 
    print("stop")      
elif(Light == "green"):
    print("you can go")
elif(Light == "Yellow"):    # elif will only check when if is not true
    print("wait there")

else:
    print("light is broken")



age = 24

if(age>=18):
    print("you can vote")
else:
    print("you cannot vote")



marks>= 90.grade=A
marks<90 >=80, grade =B
marks<80 >=70, grade = C
marks<70 and >=60 garde = d



marks = int(input("enter your marks:"))

if(marks >=90):
  grade ="A"
elif(marks>=80 and marks <=89):
    grade = "B"
elif(marks>=70 and  marks<=79):
    grade ="C"
else:
    grade = "D"

print("Grade of the student is:", grade)


#nesting 


age = 34


if(age >= 18):
    if(age>=80):
         print("you cannot drive")
    else:
         print("can drive")
else:
     print("cannot drive")



#practice question
#WAP to check if a numbe rentered by a use r is odd or even 

num = int(input("enter the number "))
rem = num % 2

if(rem == 0):
    print("even")
else:
    print("odd")


#WAP to find the gratest of 3 numbers entered by the user 


num1 = int(input("enter the number one:"))
num2 = int(input("enter the number second:"))
num3 = int(input("enter the number third:"))


if(num1>num2 and num3):
    print("Num 1 is greatest", num1)
if(num2> num1 and num3):
    print("Num 2 is greatest",num2)
else:
    print("Num 3 is greatest", num3)
"""

#WAP to check if a number is a multiple of 7 or not


num = int(input("Enter a number:"))

rem = num % 7

if(rem == 0):
    print("Divisible by 7")
else:
    print("Not divisible by 7")







