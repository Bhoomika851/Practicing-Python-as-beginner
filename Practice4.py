#LISTS - in square brackets
fruits =["apple", "mango", 5 , "kiwi", 7.2]
print(fruits)

#slicing in lists
print(fruits[2:5])        #[5, 'kiwi', 7.2]
my_list = [1, 2, 3, 4, 5] 
print(my_list[1:4])       #[2, 3, 4]
print(my_list[:3])        #[1, 2, 3]
print(my_list[2:])        #[3, 4, 5]
print(my_list[::2])       #[1, 3, 5]

#extend() - add new elements
fruits.extend(['blue',4])
print(fruits)             #["apple", "mango", 5 , "kiwi", 7.2, 'blue',4]
 
#append()   -add new sublist i.e 1 element inside it sub elements
fruits.append([1,9])
print(fruits)             #["apple", "mango", 5 , "kiwi", 7.2, 'blue',4,[1,9]]

#del()
del(fruits[0:3])
print(fruits)             #["kiwi", 7.2, 'blue',4,[1,9]]

#copy()
list = [1,2,3]
new_list = list.copy()
print(new_list)

#count()   - counts how many times a particular element is given
x = [1,2,3,2,4,2,6]
print(x.count(2))        #3

#insert()
list.insert(1,6)
print(list)              #[1,6,2,3]

#pop()
my_list = [10, 20, 30, 40, 50] 
removed_element = my_list.pop(2) # Removes and returns the element at index 2 
print(removed_element)   #30 
print(my_list)           #[10, 20, 40, 50] 

#remove()
my_list.remove(40)
print(my_list)           #[10, 20, 50]

#reverse()
my_list.reverse()
print(my_list)           #[50, 20, 10]

#sort()
a = [5,3,7,4,9,1]
a.sort()
print(a)                 #[1, 3, 4, 5, 7, 9]
a.sort(reverse=True)
print(a)                 #[9, 7, 5, 4, 3, 1]


#TUPPLES - in () parenthesis
z = ("p", 3, "r", 6, "s", 6)
print(z.count(6))        #2
print(z.index("s"))      #4
print(len(z))            #6

#sum()
print(sum(a))            #29

#min() and max()
print(min(a))            #1
print(max(a))            #9
