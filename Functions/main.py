'''

function      -> it is block of code 
              -> reusability
              -> modularity
              -> scoping
              
function will be more reliable if
---------------------------------
-> function naming tells what it does
-> Do only one task effectivily
-> avoid global variables inside function

              


parameters  -> placeholders for the values use when defining a function
arguments   -> Used when calling a function
              
function syntax
---------------

def function_name(arguments,....):
  statements
  return

function_name(parameters)

'''


def greet(name,city):
  print(f"Hello {name} you are from {city}")


greet('ramesh','kanpur')
greet(city="mumbai",name="Ajay devgan")


'''
3 types of arguments
--------------------

1) Positional Argument
----------------------

def greet(name,city):
  print(f"Hello {name} you are from {city}")

greet('ramesh','kanpur')

2) Keyword Argument
-------------------

greet(city="mumbai",name="SRK")

3) Defualt Argument
-------------------

def greet(name="Guest"):
  print(f"Welcome {name}")

greet()

'''


'''

return statement
----------------

def addition(num1=0,num2=0):
  return num1+num2

result = addition(2,5)

'''

def addition(num1=0,num2=0):
  return num1+num2

print(addition(2,5))


'''

Decorators
----------

burger -> function
extra cheese -> extra feature

-> Decorators means adding extra features without touching main function
-> Decorators takes function as a parameter


def my_decorator(func):
  def wrapper():
    print("Before the main function")
    func()
    print("After the main function")
    
  return wrapper

# One Way
---------

def hi():
  print('hI Inside in decorator')

decor_func = my_decorator(hi)
decor_func()

# Other Way

@my_decorator
def hi():
  print('hI Inside in decorator')
  
hi()


'''

def my_decorator(func):
  def wrapper():
    print("Before the main function")
    func()
    print("After the main function")
    
  return wrapper


@my_decorator
def hi():
  print('Inside the Decorator')

hi()


'''
Generator
---------

-> a type of function that behave like a iterator
-> [yield] keyword used its mean one value at a time

def count_down(num):
  while num > 0:
    yield num 
    num -= 1
    
for num in count_down(5):
  print(num)

'''

def count_down(num):
  while num > 0:
    yield num 
    num -= 1
    
for num in count_down(5):
  print(num)


'''
Lambda function
---------------

-> Anonymous function
-> make with keyword lambda
-> useful for one line task

syntax
------

lambda arguments:expression condition

add_ten = lambda x:x + 10

print(add_ten(5)) -> 15

'''


add_ten = lambda x : x + 10

print(add_ten(5))