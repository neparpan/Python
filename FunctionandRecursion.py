
#function definition
def calc_sum (a, b):#parameters
    sum = a + b

    return a + b

sum = calc_sum(5,10)#function call; arguments
print(sum)


def print_hello():
    print("hello")

output = print_hello()
print(output)


#average of 3 numbers

def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calc_avg(6,3,3)


#both on same line


print("arpan", end = " ") #seperator =" "
print("nepal") #end ="\n"



#deault parameters
#these are used when no any parameters are passed
#default arguments always comes in last

def calc_prod(a,b=3):  #by default parameters
    print(a*b)
    return a*b

calc_prod(2)


#wap to print the length of a list(list is the parameter)#in single line

cities = ["ktm","bhw","pkh","palpa"]
heroes = ["thor","ironman","cpatain america","shaktiman"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
     print(item, end=" ")

print_list(cities)
print_list(heroes)



#wap to finde thefatorial of n.(n is the parameter)

n = 5


def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)

calc_fact(5)


#Recursion
#when a function calls itself repeatedly
# prints n to 1 backwards


def show(n):
    if(n == 0):
        return   #base case
    print(n)
    show(n-1)

show(5)


# calculate factorial of n 

def fact(n):
   if(n ==1 or n==0):
      return 1
   return fact(n-1) * n

print(fact(5))




#wap to recursive function to calculate the sum of first n natural numbers.

def print_list(list, idx=0):
    if(idx == len(list)):
     return
    print(list[idx])
    print_list(list, idx+1)
fruits =["apple","litchi","apple","banana"]
print_list(fruits)