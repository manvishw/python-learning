'''
Control Statements
------------------

conditional       -> if,elif,else
loop              -> for,while
flow              -> continue,break

'''

'''
Conditional
-----------

if condition:
  statements
elif condition2:
  statements
elif condition3:
  statements
else:
  statements

'''

# input() function is built in function takes input from user and return string

# marks = int(input("Enter your Marks: ")) #Convert string to int with int()


# if marks > 90:
#   print("Excellent")
# elif marks <= 90 and marks > 80:
#   print("Good")
# elif marks <= 80 and marks > 60:
#   print("pass")  
# else:
#   print("Fail")


'''
Loops (Repition)
----------------

for            -> Repeating for some fixed range
while          -> Repeating until condition not false

for syntax:
-----------

for variable in [Any Sequence,list,tuple,dict,string]:
  statements

while syntax:
-------------

while condition:
  statements

'''

# while input("write any thing please --> "):
#   print("to stop it just press enter without writing any text")


''' 
range(start,end[exclusive],step) 
python built in function 
'''

# for i in range(1,101,1):
#   if i % 2 == 0:
#     print("Even Number : ",i)
#   elif i == 51:
#     break
#   else:
#     print("Odd Number : ",i)