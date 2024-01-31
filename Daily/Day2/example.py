#conditionals - x > 10 turns into a boolean. It's a test of a variable if it has a specific value
    # > (greater than) , == (compare two things to see if they are the same), >=, <=, etc
        # x == y is true if x is the same as y
        # x != y is true if x is NOT the same as y

#if condition:
    #commands
#elif conditional: (if conditional is false)
    #commands
#else: (elif conditional is false)
    #commands

#while condition:          - indefinite iteration, doens't know when it's ending
    #commands

#for *x* in *iterable*:        - definite iteration, knows when it's ending
    #commands
    #used for stepping down lists. It gets run one time for everything in the list
#ex.
#for x in li:
    #(li is [1,2,3])
    #once with x = 1
    #once with x = 2
    #once with x = 3

# print out a message indicating if the value of my_int is positive, negative, or zero
"""
my_int = 4

if my_int > 0:
    print("positive")
elif my_int < 0:
    print("negative")
else:
    print("zero")

# print out each number between starting_num and ending_num

starting_num = 12
ending_num = 21
x = starting_num
for x in range(starting_num, ending_num):
    x = x + 1
    print(x)

# print out whether or not requested_room is in the list of classrooms


classrooms = ["TSC213", "TSC221", "TSC223", "TSC101", "TSC127"]

requested_room = input("Which classroom would you like to reserve?: ")

if requested_room in classrooms:
    print("This is a classroom.")
else:
    print("This is not a classroom.")


# print out only the element of grades that is the highest

grades = [45.3, 83, 77.3, 61.9, 70]
grades.sort()
x = grades[-1] #grabs last number in list, counted backwards from the last number
print(x)
# print the average group size

group_sizes = [3, 4, 2, 3, 3, 2, 4, 2, 3]
added = sum(group_sizes) / len(group_sizes)
print(added)

added = 0
for size in group_sizes:
    added += group_sizes
    print(added / len(group_sizes))


"""
string_a = "here is one string"
string_b = "and now another"

result = 0

for a in string_a:
    if a in string_b and a != " ":
        #if a == " ":
        #    pass #do nothing
        #else:
            result += 1

print (result / len(string_a.replace(" ","")))
# compute and print what percentage of the letters in string_a are also in string_b
