"""
# while loops

count =1 

while count <=5:
    print("hello", count)
    count += 1


    i = 1
    while i<=5:
        print("arpan", i)
        i += 1


# prints number from 1 to 5

    z =1 
    while z <=5:
     print(z)
     z +=1

    
#print umber in reverse
    
    y = 5
    while y >= 1:
       print(y)
       y -= 1

#print number from 1 to 100
a = 1
while a <= 100:
       print(a)
       a += 1

# print numbers from 100 to 1

b = 100
while b >=1:
       print(b)
       b -= 1


# print the multipliccation table of a number n 

n = int(input("enter a number:"))
i = 1
while i<=10:
    print(n*i)
    i +=1



# print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]


a =1
while a <=10:
    print(a*a)
    a += 1

heroes =["ironman", "thor", "superman", "batman"]

idx = 0
while idx <len(heroes):
    print(heroes[idx])
    idx += 1


#search for a number x in this tuple using loop
# [1,4,9,16,25,36,49,64,81,100]

nums =  [1,4,9,16,25,36,49,64,81,100]

x = 36

i =0
while i < len(nums):
    if(nums[i] == x):
        print("Found at index", i )
    i += 1




# Breaks and continue

i = 1
while i <= 5:
    print(i)
    if(i==3):
        break
    i += 1



i = 0 
while i <= 5:
    if(i==3):
        i +=1
        continue
    print(i)
    i += 1





# for loops
# used for sequential travesal. for traversing list, string, tuples etc

nums =  [1,2,3,4,5]

for val in nums:
    print(val)


vegetables =["potato","brinjal","ladyfinger","cucumber"]

for val in vegetables:
    print(val)



tup = (1,2,3,4,2,8,9)


for num in tup:
    print(num)



str ="arpannepal"

for char in str:
    if(char == 'e'):
        print("e found")
        break
    print(char)
else:
    print("end")



#practice question
# print number by loop

nums = [1,4,9,16,25,36,49,64,81,100]

for el in nums:
    print(el)


# search for the number x in this tuple using loop
# [1,4,9,16,25,36,49,64,81,100]

nums = (1,4,9,16,25,36,49,64,81,100,49)

x = 49

for el in nums:
    if(el == x):
        print("49 found")
    else:
        print(el)




# RANGE 
# returns a sequence ofnumbers, starting from 0 by default, and increments by 1(bydefault and stops before a specified number.


seq = range(5)


for i in seq:
    print(i)



for i in range(10):#range(stop)
    print(i)



for i in range(2,10):#range(start,stop)
    print(i)



for i in range(2,10,2):#range(start,stop,step)
    print(i)


#wap to find sum of first n naturalnumber(using while)


n = 7
sum = 0
i =1


while i<= n:
       sum += i
       i += 1

print("total sum is:", sum)
"""

#wap to find the factorial of first n numbers(using for)

n = 5
fact = 1
i =1


while i<= n:
       fact *= i
       i += 1

print("Factorial:", fact)