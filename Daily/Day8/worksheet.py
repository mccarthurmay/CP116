from functools import reduce
#1
my_list = [5, 7, 9, 10]
def my_max(x,y):
    if x > y:
        return x
    else:
        return y

result = reduce(my_max, my_list)

print(result)


my_list = [3, 5, 8, 13, 21, 32, 2012]

#2
new_list= []

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

new_list = list(filter(is_even, my_list))

print(new_list)

#3

my_list = [-1, 20, -4, 5, 32, -64]

result = 0


def is_neg(x):
    if x < 0:
        return True
    else:
        return False

def my_sum(x,y):
    return x+y

result = reduce(my_sum, filter(is_neg, my_list))

print(result)

#4

nested_list = [[1,2,3], [4], [5,6,7,8], [30, 40]]

result = [ ]

print(result)

def my_square(x):
    return x**2
def map_square(in_list):
    return list(map(my_square, in_list))

result = list(map(map_square, nested_list) )#map "map_square" over "nested_list"

print(result)
