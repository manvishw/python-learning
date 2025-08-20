'''
Exception Handling
------------------

1) compile time error
---------------------
-> When writting code,Syntax Error

2) runtime error also known as Exception

-> Error Occurs during runtime
-> Divide by Zero famous

3) logical error

-> Program works fine but not given desired output
-> It Fails on Logically


Erros occurs in software known as [Bugs]
Removing or fixing these errors known as [Debugging]

Handling Exception
------------------

try-except block
-------x--------

try block       => you sure that this block raises any error
except block    => Catch That arises error from try block 
                   and handle it
                   
syntax
------

try:
  statement
  error occured chances
except Exception:
  handle Exception
finally:
  Close memory for DB
  Always run if error arise or not


'''

class CustomError(Exception):
  pass


try:
  raise CustomError("My Error")
except ZeroDivisionError as e:
  print(e)
except ValueError:
  print('string')
except TypeError: 
  print("Different Types")
except Exception as e:
  print(e)
finally:
  print("Connection Closed")