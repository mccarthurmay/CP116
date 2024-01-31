

"""
def f(x):
    global a #check the global scope for something with a... so a = 20 now instead of nothing
    # also making a global variable a
    a = x



a = 20
print(a)
f(30)
print(a)

#namespace/scope is the collection of variables that our code can see
#   -order o fnamespace
#   -local - wherever our code is currently executing
#   -Enclosing - ???
#   -Global - everything defined in our program
#   -Built-in - things that are part of python
#       - like input()... so if we assign x to input (input = x), since this is last, it'll find input in global

#classes/object
#   - holding lots of pieces of info - nouns/adj
#   - do stuff - verbs
#   - it's a type

#class myclass():   #has its own namespace
#   def __init__(self):
#       self.color="brown"  #color is a variable

"""

class Dog():
    #constructor for dog class
    def __init__(self, loudness = 5, color="brown"):
        self.color = color
        self.loudness = loudness
    def bark(self):
        if self.loudness > 5:
            print("woof")
        else:
            print("bark")

buckaroo = Dog(loudness = 9, color="brindle") 
manny = Dog()   #two specific namespaces, no color= means it's default brown
manny.color = "grey"
print(buckaroo)
buckaroo.bark() #calls method in class, uses buckaroo namespace not manny namespace
manny.bark()
