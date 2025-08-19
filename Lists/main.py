'''
List  -> ordered dynamic array
      -> Support Multiple data types
      -> mutable
      -> start with 0 index
      -> with + operator you can concate lists
      -> with * operator you can repeat list 
      
4 ways to Create a list
-----------------------
'''

'''
1) Using [] Brackets
---------------------
my_list = [1,2,3,"Hello",True]
 
'''

my_list = [1,2,3,4,"Hello",True]
print(my_list)

'''
2) Using list() Constructor
---------------------------

my_list = list([1,2,3])

'''

my_list2 = list([1,2,3,4])
print(my_list2)


'''
3) List Comprehension 
---------------------

my_list = [x for x in range(1,11)]

'''

my_list3 = [x for x in range(10,32) if x % 2 == 0]
print(my_list3)


'''
4) Using range() function
-------------------------

my_list = list(range(1,101))

'''

my_list4 = list(range(40,51))
print(my_list4)

'''
Accessing List Element
----------------------
list[index]

Slicing List
------------

list[start:end:step]

'''

print(my_list[4])
print(my_list[::-1])


'''

List Methods
------------

list.append(3)                    => Add on last
list.extend(list)                 => extend list 
list.insert(index,value)          => add element in given index
list.remove(value)                => remove given value in list if exists
list.pop(index)                   => remove last element when index is not given it return popped value
list.clear()                      => clear all elements in list 
list.index(value)                 => get index of given value in list
list.count(value)                 => return count how much time given element occur in list
list.sort()                       => Sort the list in ascending Order
list.reverse()                    => Reverse the list
list.copy()                       => Copy list return new list value which is not dependent on copied list
min(list)                         => Find Minimum value and return it
max(list)                         => Find Maximum value and return it



'''

