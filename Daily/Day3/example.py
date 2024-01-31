#mylist = [0,10,5,-1,-128,0]   (indicies go like 0,1,2,3,4,5)
#mylist[2] - looks inside list under the indexed entry at 2 (starting from 0)
#   - mylist.append() adds things into lists
#   - also mylist = mylist + [3] - concatinate
#       - insert method mylist.insert(3,108) insert at fourth location, old fourth goes forward,  and insert 108
#   - mylist[:3] is everything up to 4th (noninclusive), mylist[3:] everything from the 4th spot onward (inclusive)
"""
mylist = [0,10,5,-1,-128,0]
print(mylist[3])
mylist.insert(3,108)
print(mylist[3])
print(mylist)
print(mylist[:3])
print(mylist[3:])


#dictionary
my_dict = {}
my_dict[2] = 56
#      key = Value
my_dict["dog"] = "meow"
my_dict["cat"] = 25
#      keys can be anything, value can be anything. They can only have ONE value assigned.
print(my_dict)
my_dict["dog"] = "bark"
print(my_dict)
#preset dict
my_other_dict = { "no":"more", 2:5, 6:2}
print(my_other_dict)
#preset dict with dict inside dict inside dict
#my_other_other_dict = {
print(my_other_dict)
#can't concatinate dictionaries; they may share a key (my_otherdict and mydict)
#updates my_dict, replacing 2 key and adds all new keys
my_dict.update(my_other_dict)
print(my_dict)
#^ alters my_dict, but is JUST an action. Does not hand anything back if the action is printed
print(my_dict.update(my_other_dict))


#ERROR SKIPPER

#try:
    #risky code
#except:
    #recovery code



def my_cool_thing(input1, input2):
#keyword #name of function #input expected to see

    #do stuff with input1 and input2

return #results_____
#keyword


#0+1 = 1 1+1=2 1+2=3 3+2=5 3+5=8
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("gimme"))
print(fib(n))

x = 1
while x == 1:
    name = input("input name: ")
    name = {}
    if name == "face":
        print(name)
        print(max)
        print(ma)

"""

# Python3 code to demonstrate working of
# Getting first key in dictionary
# Using keys() + list()

# initializing dictionary
test_dict = {'Gfg': 1, 'is': 2, 'best': 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using keys() + list()
# Getting first key in dictionary
res = list(test_dict.keys())[0]

# printing initial key
print("The first key of dictionary is : " + str(res))
