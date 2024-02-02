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

#map: map takes in a function and a a list and applies that function
#to every element of the list. Return Map data type
from functools import reduce


def f(x):
    return x+1
my_list = [2,3,5,6,7,11,12,23]




#new_list = []
#for x in my_list:
    #new_list.append(f(x))

#same as above
new_list = list(map(f, my_list))
print(new_list)


#filter: filter takes in a function and a lisst, applies that function to everything
#in the list, and only keeps entries where the function evaluates to TRUE

my_list2 = [0,1,1,1,2,3,4,5,6,22]

def is_even(x):
    if x % 2 == 0: #remainder thing, if remainder is 0 when dividing 2
        return True
    else:
        return False

#new_list2 = []
#for num in my_list2:
    #if is_even(num):
        #new_list2.append(num)

new_list2 = list(filter(is_even, my_list2))
print(new_list2)

#reduce: takes in a function of two inputs, and repeatedly uses that function
# to combine elements of a list

my_list3 = [0,1,1,1,3,4,5,6,10]

result = 0
result1= 0

for number in my_list3:
    result += number

print(result)



def my_sum(x,y):
    return x+y

result1 = reduce(my_sum, my_list3)

print(result1)
