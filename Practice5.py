#Dictionaries
Dict = {"key1": 4, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6 }
print(Dict)
print(Dict["key1"])             #4
print(Dict[(0, 1)])             #6
print(Dict.keys())
print(Dict.values())

Dict['key9'] = '5'
print(Dict)        #append

#del()
del(Dict["key1"])
print(Dict)

#Sets
list1 = ["pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"]
set1 = set(list1)
print(set1)
#set1 = {'R&B', 'disco', 'hard rock', 'pop', 'rock', 'soul'}

#add()
set1.add("kiss")
print(set1)

#remove()
set1.remove("hard rock")
print(set1)

#intersection
set2 = {"kiss", "hugs", "pop", "rizz"}
intersection = set1 & set2
print(intersection)                   #{"kiss", "pop"}

#difference
diff = set1.difference(set2)
print(diff)                           #{'soul','R&B','disco','rock'}

#union
U = set1.union(set2)
print(U)
