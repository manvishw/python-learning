'''
Dictionary    -> Key-value pair
              -> Unordered until python 3.7 but not it is ordered
              -> mutable
              -> dynamic        
'''

my_dict = {
  "name":"Manas Vishwakarma",
  "age":23,
  "gender":"Male",
  "isGraduated":True,
  "cgpa":8.03  
}

print(my_dict)

# Accessing value
print(my_dict["name"])

# Adding new value
my_dict["dob"] = "22/12/2002"
print(my_dict)

# Updating existing Element
my_dict['age'] = 24
print(my_dict)

# Deleting existing Element
del my_dict["dob"]
print(my_dict)


'''
Dictionary Methods
------------------

dict.get(key,'default value')           -> Get value from given key
dict.keys()                             -> Return all keys on dictionary
dict.values()                           -> Return all Values on dictionary
dict.items()                            -> Return keys,values both on dictionary
dict.pop(key,'default')                 -> remove value on that given key and return removed value
dict.popitem()                          -> remove last pair of dictionary
dict.clear()                            -> Clear Dictionary

'''


'''
Dictionary compehension
-----------------------

squares = { x : x*x for x in range(1,6)}

'''


'''
looping on dictionary
---------------------

for key in my_dict:
  print(key)

for value in my_dict.values():
  print(value)
  
for key,value in my_dict.items():
  print(key,value)


'''

for key,value in my_dict.items():
  print(key,value)