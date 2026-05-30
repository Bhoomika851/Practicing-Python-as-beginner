#Indexing in String
#starts from 0

name = "Bhoomika"
print(name[0])        #B
print(name[6])        #k

#negative indexingnew_func
#starts from -1 backwards
print(name[-1])       #a
print(name[-8])       #B

#Length of string
print(len(name))      #8
print(len("New York"))#8

#Slicing (the first no. is index value and second number is length value)
print(name[0:3])      #Bho
print(name[4:7])      #mik

#Stride
print(name[::2])      #Bomk   #every 2nd element
print(name[0:5:2])    #Bom    #every 2nd element till index 4
print(name[::3])      #Bok    #every 3rd element

#Concatenate two string
temp = name + " is smart."
print(temp)           #Bhoomika is smart.
print(3*name)         #BhoomikaBhoomikaBhoomika

#Escape Sequences
print("name\ndamn")            #\n= new line
print("name\tcool")            #\t= Tab or space
print(r"name\tcool")           #r makes the string raw as given

#String operations
#upper()
Upper = name.upper()
print(Upper)          #BHOOMIKA

#lower()
f2="YOU ARE RIGHT"
f2.lower()            #you are right

#replace()
a = "Harshita is cute."
Replace = a.replace('Harshita',name)
print(Replace)        #Bhoomika is cute.

#find()
Find = name.find("oomi")
print(Find)           #2       #output is 1st index of sequence
Find = name.find("dfhhk")
print(Find)           #-1      #if substring is not in string, O/P is -1

#split()
a= "The Great Britain"
Split = a.split()
print(Split)           #['The', 'Great', 'Britain']
