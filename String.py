str1 = "this is a string .\n we are creating it in python"

str2 = 'Arpan nepal'

str3 = """this is a string"""



print(len(str2))#length of string
print(str1)
print(str2+str3)#concatenation


#Indexing

ch = str1[0]
print(ch)


#Slicing

print(str2[1:4])


#Negative Index


print(str2[-5: -1])

# string Function

str = "i am studying python from apna college"
print(str.endswith("ege")) #returns ture if string ends with substr


print(str.capitalize()) # capitaliize the first letter once only
print(str)# This does not hold the capitalization 
str = str.capitalize()
print(str)# capitalize and store it in the original string



print(str.replace("o","a"))#it replace o with a 


print(str.find("o"))#finds the first o and return its index


print(str.count("from"))# tells how many times froom comes in our string



#practice question 
#wap to input users frist namme and print its length 


name =input("enter first name :")
print("length of your name is:", len(name))



#wap to find the occurences of $ in a string 


str = "hi, $i am the $symbol $99.99"
print(str.count("$"))




