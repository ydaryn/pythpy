import os
#ex1
fold=os.listdir()
print(fold)

#ex2
path=os.getcwd() #or other path, because current path is already read/writable
if os.access(path, os.F_OK):
    print("exist")
else:
    print("not exist")
    
if os.access(path, os.R_OK):
    print("readable")
else:
    print("not readable")
    
if os.access(path, os.W_OK):
    print("writable")
else:
    print("not writable")
      
if os.access(path, os.X_OK):
    print("execute")
else:
    print("not execute")
    
#ex3
import os
path=os.getcwd()
if os.path.exists(path):
    print("exists")
    filename = os.path.basename(path)
    direct = os.path.dirname(path)
    print(filename)
    print(direct)
else:
    print("doesnt exist")   
    
#ex4
file_path="demofile.txt"
with open(file_path, 'r') as file:
    line_count = 0
    for line in file:
        line_count += 1
print(line_count+1)

#ex5
import os
MyList=[1,2,3,4,5,6]
with open("demofile.txt", 'w') as file:
    for i in MyList:
        file.write(str(i)+', ') 
        
#ex6
import os
import string 
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in alphabet:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("This is file " + filename)
        
#ex7
with open('source.txt', 'r') as source:
    with open('receiver.txt', 'w') as receiver:
        receiver.write(source.read())
        
#ex8
file_path = os.getcwd() 
file_name = "name_of_file.txt" 
file_to_delete = os.path.join(file_path, file_name)  
if os.path.exists(file_to_delete) and os.access(file_to_delete, os.X_OK):
    os.remove(file_to_delete)
       