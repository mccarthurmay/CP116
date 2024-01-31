#load shakes.txt as string
#use python's "open" function

msnd = open("shakes.txt")
#read contents of file with ".read()" and saving into "contents"
contents = msnd.read()

#ask user to input character

target = input("Which character are you looking for? ")
split_play = contents.split(target)
print(len(split_play) - 1)
#split play into scenes
#count number of times character appears in the scene
