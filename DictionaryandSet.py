#dictionary are ued to store data values in key:value pair
"""
info ={
    "name" : "arpan nepal",
    "age" : 23,
    "marks" : [98, 97, 95],
    "subjects" : ["pthon", "c", "java"],
}

print(info)



# Nested Dictionary


student ={
    "name" : "rahul kumar",
    "score" :{
        "phy" :98,
        "chem" :97,
        "math" :95
    }
}

print(student)
print(student["score"] ["chem"]) #print the marks of chem 



#Dictionary Methods



print(student.keys())
print(list(student.keys())) #print the output in list 
print(len(student))

print(student.values())

print(student.items())

pairs = list(student.items())
print(pairs[0])
print(pairs[1])


print(student["name"])  #ERROR
print(student.get("name")) #NO ERROR --> NONE


new_dict = ({"city": "ktm", "age" : 21})
student.update(new_dict)


new_dict = ({"name": "rajesh", "age" : 21})  #now the name wil change
student.update(new_dict)
print(student)




# Sets
#set is a colletion of the unordered items

#collection = {1,2,3,4, "hello", "world"}
collection = {1,2,2,2, "hello", "world"}
collection1 = set()  # empty set
collection1.add(1)
collection1.add(2)
collection1.add(3)
collection1.add("arpan nepal")
collection1.add((4,5,6))
collection1.remove(2)
#collection.clear()
print(len(collection))
print(collection.pop())



set ={1,2,3}
set2 ={3,4,5}

print(set.union(set2))#1 2 3 4 5
print(set.intersection(set2))# {3}



print(collection)
print(type(collection))
print(len(collection)) #totalnumber of items
print(collection1)
print(type(collection1))






# Practice Question 



#Wap to store dollowing in python dictionary
#table: "a piece of furniture", "list of fact & figures"
#cat : "a small animal"



dictionary ={
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts and figures"]
}

print(dictionary)
"""

#wap to find that how many classrooms are needed by all students . assume one classroom is required for 1 subject
# "python", "java","c++","python","javascript",
#  "java","python","java","c++","c"

subjects = {
    "python", "java","c++","python","javascript",
    "java","python","java","c++","c"

}
print(len(subjects))

