'''

String  -> Sequence of Characters
        -> String is immutable
        -> String is indexed like list and also iterable
        -> multiply string its value print that time
        -> two string concate with + 
        
        

single quote string -> ''
double qoute string -> ""
multiline string ->""" Inside it"""

'''

# single_qoute = 'single'
# double_qoute = "double"
# multiline_str = """we write anything inside it very large text
# """

# print(single_qoute,"\n",double_qoute,"\n",multiline_str)


'''

len()         -> count length of string with also spaces
'''

# password = input("Enter password : ")

# if len(password) > 8:
#   print("Password is Strong : ",password)
# else:
#   print("Weak Password\nHave at least 8 characters")


'''
Slicing
-------
string[start:end[exclusive]:step]
'''

text = "ThisisStringSlicingSection"

# print(text[::-1]) # reverse it
# print(text * 2)


'''

str.lower()                           -> convert in lowercase
str.upper()                           -> convert in Uppercase
str.capitalize()                      -> First Character is Capital
str.title()                           -> On sentence it capitalize first letter of every word
str.swapcase()                        -> change character with opposite cases [lower to upper,upper to lower]
str.find('value')                     -> find given value in string and return index of first occurance
str.replace(old_value,new_value)      -> Replace old value with new string
str,split(",- ")                      -> split character based of symbol[, - space] return list
str.join(list)                        -> join as string 
str.startswith('string')              -> True if it start with that String
str.endswith('string')                -> True if it end with That String
str.isalpha()                         -> True if all characters are alphabetics (if there is space then it return False)
str.isdigit()                         -> True if all characters are digits like [12,3,4]
str.isalnum()                         -> True if string have mixed characters


'''
print(text.isalpha())
