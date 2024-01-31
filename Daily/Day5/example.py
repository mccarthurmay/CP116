#                                                               function
#def function(parameters):
#   - do stuff with parameters
#   - return something

#verb - an action that you call upon to execute something
#recipe - holds stuff to do when you want to

#want to do some action over and over
#if our program has multiple verbs
#want to process data

#                                                               class
#class classname():
#   - def __init__(self)
#       - do something

#data types that we define
#bundle together several pieces of information
#group of functions


#when we need to keep track of several things at once
#multiple verbs for the same noun



#                                                                packages/module
#import package
#from package import (smaller section)

#folder containing lots of code that someone else wrote


#lets us do interesting stuff with premade things
#we don't have to code it from bottom up


#                                                               NumPy
#numerical python
#allows us to do fancy and fast math with 2D arrays
#2D array is a table of numbers [1,0,2,3,4,5] with more than one row
#             MATRIX            [2,100,5006,0]
import numpy as np


arr1 = np.array(
    [
        [0,   1],
        [1,   0]
    ]
)

arr2 = np.array(
    [
        [4,  5],
        [-10, 2]
    ]
)
print(arr1)
print(arr2)
print(arr1 + arr2) #adding numbers where they are adjacent in other matrix
print(arr1 + 1) #added one to every entry
big_arr = np.random.random((10,12))  #random 10x12 array
print(big_arr)
#slice an array
print(big_arr[3:6, :2]) #rows 3-5, columns up to 2
big_arr[3:6, :2] = 0
print(big_arr)



#
