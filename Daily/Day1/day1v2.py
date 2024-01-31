#load shakes.txt as string
#use python's "open" function

msnd = open("shakes.txt")
#read contents of file with ".read()" and saving into "contents"
contents = msnd.read()

#ask user to input character

target = input("Which character are you looking for? ")

#split_play = contents.split(target)
#print(len(split_play) - 1)

# split into acts

split_act = contents.split("ACT ")

for j in range(1, len(split_act)):
    act = split_act[j]
    #split act into scenes
    split_scene = act.split("SCENE ")
    #for each scene
    for i in range(1, len(split_scene)):
        #get the ith scene
        scene = split_scene[i]
        #test if the target char is in the scene
        if target in scene:
            print(target, "is in Act ", j ," is in Scene ", i)



# split each act into scenes

# for each scenes
    #if the target character is in that scene, print scene and act
#
