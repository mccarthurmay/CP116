#Goal: find the average height of each category of medalist

#read and open filename
file_open = open("olympic_medals.tsv")
file = file_open.read()

file_split = file.split("\n")
#loop through lines in the file
#for each line:
height_bronze = 0
height_silver = 0
gold_list = []
count_bronze = 0
count_silver = 0

for line in file_split[1:]: #range to last line
    #reads individual lines
    items = line.split("\t")
    try:
        height = int(items[3])
        medal = items[-1]
        if medal == "Bronze":
            height_bronze = int(height) + height_bronze
            count_bronze = count_bronze + 1
        if medal == "Silver":
            height_silver = int(height) + height_silver
            count_silver = count_silver + 1
        if medal == "Gold":
            gold_list.append(height)
    except:
        pass


avg_bronze = height_bronze/count_bronze
avg_silver = height_silver/count_silver
avg_gold = sum(gold_list) / len(gold_list)

print(avg_bronze, avg_silver, avg_gold)
    #split the line by tabs
    #get the height and medal info by using indices 3 and -1
    # store those pieces of info


#store information
