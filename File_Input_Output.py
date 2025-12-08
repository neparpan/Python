#open ,read and close file
#we have to open file before reading and writing

# r, w, x, a, b, t, +, r+, w+, a+

f=open("Demo.txt", "r")
data = f.read() # reads entire file 
print(data)

data = f.read(5) # reads frist five letters
print(data)

data = f.readline() #reads one line at atime
print(data)

line2 = f.readline(2)
print(line2)# print the line 2

f.close()


#writing to a file
#"a "  append at the end


f= open("Demo.txt","w")

f.write("I want to learn javascript tomorrow. 456")# override the whole docs

f.close()



f= open("Demo.txt","a")

f.write("\nI want to learn python tomorrow. 456")# adds this line in docs

f.close()




f = open("demo.txt", "r+")
f.write("abc")
print(f.read())
f.close()



#with syntax


with open("Demo.txt", "r") as f:
    data =f.read()

with open("Demo.txt", "w") as f:
    f.write("new data")



#deleting a file
# using the os module

import os

os.remove("Demo.txt")





# practice question


with open ("practice.txt", "w") as f:
  f.write("hi every one\n i am learning python\n")
  f.write("using java.\n I like programming in python.")


with open ("practice.txt", "r") as f:
    data = f.read()
    new_data= data.replace("python", "java")
    print(new_data)

with open ("practice.txt", "w") as f:
   f.write(new_data)


def check_for_word():
   word = "xlearning"
   with open("practice.txt", "r") as f:
      data = f.read()
      if(word in data):
         print("Found")
      else:
         print("not found")

def check_for_line():
   word= "learning"
   data = True
   line_no =1
   with open("practice.txt", "r") as f:
      while data:
         data = f.readline()
         if(word in data):
            print(line_no)
            line_no += 1