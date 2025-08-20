from abc import ABC,abstractmethod
'''
Before OOPS problems were faced:
--------------------------

1) Code Duplication
2) Code Maintenence is difficult
3) Data Security Issues
4) Poor Code Reusability
5) No real world representation


OOP -> Object Oriented Programming
    -> It is Paradigm that helps to solve real world problems
    -> Provide Security,Maintenability,Reusability
    -> Best Choice for large Projects

class   -> A class is a Template or Blueprint for creating objects
Object  -> Actual Instance of a class
            -> 1) Properties/attributes
            -> 2) Functions/Behaviours


Syntax
------

class Character:

    def __init__(self.name,health):    => Constructor Function
      self.name = name                 => self represent to that class
      self.health = health 

warrior = Character("Shazam",100)
print(warrior.name) 


4 major OOPS Concepts
---------------------

1) Inheritance
--------------

-> Child class Inherit properties and methods from Parent CLass
-> 

class Animal:
  def speak(self):
    print("Animal Make Sound")

class Dog(Animal):
  def bark(self):  
    print("Bark")

dog = Dog()
dog.bark()
dog.speak()  => Inherits



2) Encapsulation
----------------

-> Hiding actual logic from the user
-> Showing Necessary Info Only

class Bank:
  def __init__(self,account_number,balance):
    self.account_number = account_number
    self.__balance = balance    => Private Method Can't access by user
  


3) Polymorphism
---------------
-> one name, many forms
-> A person can be father and it also an employee

class Bird:
  def sound(self):
    print("Birds Make Sound")

class Crow(Bird):
  def sound(self):
    print("Caw Caw")

class Parrot(Bird):
  def sound(self):
    print("squawk")
    
bird1 = Crow()
bird2 = Parrot()

bird1.sound()
bird2.sound()


4) Abstraction
--------------

-> Abstract methods on abstract class 
-> method should be defined but not implemented
-> child class who inherit the abstract class should
   be implement all abstract methods
-> Abstract class object not created
-> To make abstract class it should inherits the ABC class which is 
   provided in module abc
-> Making abstract method import abstractmethod decorator

from abc import ABC,abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def start(self):
    pass

class Car(Vehicle):
  def start(self):
    print("Start Engine")
    
    
c = Car()

c.start()

  
'''


class Student:
  
  def __init__(self,name,age,gender,cgpa):
    self.name = name
    self.age = age
    self.gender = gender
    self.cgpa = cgpa



std = Student(name="Manas",age=23,gender="Male",cgpa=8.03)
std2 = Student(name="Laxman",age=22,gender="Male",cgpa=7.6)

print(std.name)
print(std2.name)


class Bird:
  def sound(self):
    print("Birds Make Sound")

class Crow(Bird):
  def sound(self):
    print("Caw Caw")

class Parrot(Bird):
  def sound(self):
    print("squawk")
    

bird1 = Crow()
bird2 = Parrot()

bird1.sound()
bird2.sound()


class Bank:
  def __init__(self,account_number,balance):
    self.account_number = account_number
    self.__balance = balance
  
  def deposit(self,amount):
    self.__balance += amount
    print(f"{amount} is Successfully Deposited!")
  
  def withdraw(self,amount):
    self.__balance -= amount
    print(f"{amount} is Successfully withdrawn")
  
  def getBalance(self):
    print(f"Balance : {self.__balance}$")
    

bank1 = Bank(160,1250.0)
bank2 = Bank(161,500.0)


bank1.getBalance()
bank1.deposit(2000)
bank1.getBalance()

bank1.withdraw(500)
bank1.getBalance()



class Vehicle(ABC):
  @abstractmethod
  def start(self):
    pass

class Car(Vehicle):
  def start(self):
    print("Start Engine")
    
    
c = Car()

c.start()