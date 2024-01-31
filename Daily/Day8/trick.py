#first trick: lambda function

def f(x):
    return x**2

lambda x: x**2

    #same thing

#python's sorting function "sorted"

my_strings = ["dog", "max", "fart", "meowg"]

print(sorted(my_strings))

print(sorted(my_strings, key=len))

def has_a(x):
    if "a" in x:
        return True
    else:
        return False

    #same thing

print(sorted(my_strings, key = lambda x: "a" in x))


#dictionary with default evaluaes


my_dict = {}
my_dict["dog"] = 8
my_dict["max"] = 10
my_dict["fart"] = 5

print(my_dict.get("tiger", 5))




#more compact list processing
my_strings = ["dog", "cat", "aardvark", "tiger"]
print([item.upper() for item in my_strings])


#list directories

import os
print(os.listdir(".")) #. = current folder
print(os.getcwd())

#getting arguments from command line
import sys
arg_list = sys.argv[1:]

#remove duplicates from list
my_strings = ["dog", "dog", "cat"]
print(my_strings)
print(set(my_strings)) #set can only contain one of each (basically a list)
