"""
#in list we can store different type (integer, float, string,etc)
#lists are mutable(change)

marks =[94.4, 87.5, 66.4, 45.1]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])


student = ["arpan", 95, 23, "ktm"]
print(student[0])
student[0] = "nischal"
print(student)


#list Slicing


marks = [87, 64, 33, 95,76]

print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[-3:-1])

#List Method

list = [1,4,3,5]

print(list.append(6))
print(list.sort())
print(list.sort(reverse=True))
print(list.reverse())
print(list.insert(1,2)) 
print(list)
print(list.remove(6))
print(list.pop(2))
print(list)



# Tuples

tup =(87,64,33,95,76)

# tup[0] =43  not allowed in python
print(tup)
print(tup[1:3])
print(tup.index(64))
print(tup.count(95))




#practice question
#wap to ask the user to enter name of their 3 favorite movies and store them in list 


movies=[]

movies.append(input("enter the name of 1st movies:"))
movies.append(input("enter the name of 2nd movies:"))
movies.append( input("enter the name of 3rd movies:"))

print(movies)


# wap to check if a list contains a palindrome of elements (plaindrome: same from back and front side)
#eg:   [1,'abc','abc',1]

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 =list1.copy()
copy_list1.reverse()


if(copy_list1== list1):
    print("palindrome")
else:
    print("not palindrome")




#wap to count the number of students with grade  A in the followinf tuple

tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))

    """


#sort the above values in a list and store them from "A" to "D"

list = ["C","D","A","A","B","B","A"]

print(list.sort())
print(list)







 




