'''
Tuple     -> Immutable
          -> mixed data type stored

some methods used with tuples
-----------------------------
-> len()
-> min() , max()
-> count()
-> index()
-> sorted(list,tuple)
          

'''

'''
Creating Tuple with ()
----------------------

my_tuple = (1,2,3,"ello")

'''

my_tuple = (1,2,4,"Hello")
print(my_tuple)

'''
Creating Tuple with tuple() constructor
---------------------------------------

my_tuple = tuple((1,2,3))

'''

my_tuple2 = tuple((1,2,3))
print(my_tuple2)

print(len(my_tuple))
print(min(my_tuple2))
print(max(my_tuple2))
print(my_tuple.count(2))
print(sorted(my_tuple2))
print(my_tuple.index("Hello"))