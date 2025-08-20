import os,pathlib

current_directory = os.path.dirname(__file__)

'''
File Handling
-------------

there are two primary file types

-> text files (.txt, .csv)
-> binary file (.png , .mp3 , etc)

First Operation is Opening File
-> For that purpose open() function exists

open("file name with path ","mode")

modes
----

r   = For reading File Content
w   = Write Mode
a   = Data is added in end 

'''


try:
  file = open(current_directory+"/files.txt",'r')

  for line in file.readlines():
    print(line)
except Exception as e:
  print(e)
finally:
  file.close()
  
  
try:
  file = open(current_directory+'/test.txt','w')
  
  file.write("Writing Some data in File")
except Exception as e:
  print(e)
finally:
  file.close()