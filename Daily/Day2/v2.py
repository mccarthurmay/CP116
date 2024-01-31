#Goal: find the average height of each category of medalist

#read and open filename
file_open = open(olympic_medals.tsv)
file = file_open.read()

file_split = file.split("\n")
#loop through lines in the file
#for each line:
y = 0
bronze_count = []
silver_count = []
gold_count  = []

for f in file_split[1:]: #range to last line
    #reads individual lines
    items = line.split("\t")


    height = items[3]
    medal = items[-1]

    if medal == "Bronze":
        bronze_count.append(height)

    #split the line by tabs
    #get the height and medal info by using indices 3 and -1
    # store those pieces of info


#store information
