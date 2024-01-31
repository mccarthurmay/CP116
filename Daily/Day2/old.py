#when i look up noc code for a country, I should get a number
    #modify or add to this number
import re
#Open and parse the data to compute the medal counts for all NOC codes
file = open("olympic_medals.tsv")
om = file.read()
#Prompt the user for a NOC of interest
noc = input("Input NOC of interest:   ")
#split om into lines and columns
#using re.split() to split with two separators - had trouble splitting more than once https://pynative.com/python-regex-split/
split_om = re.split(r"\t|\n", om)
#split_om = om.split("\t")
noc_dict = {}
medal_dict = {}
#read medal type and noc
#   - for loop
#       - skip first 13 words
#       - NOC is 7th word, metal is the 13th
x = 13 #13th is the last word of first line(metal)
y = 13
#for data in range(y):
for data in split_om:
    #make a dictionary for each country
    #NOC dictionary creation
    x = x + 7
    #print(split_om[x])
    noc_data = split_om[x]
    noc_dict[noc_data] = ""

    x = x + 7

    if x == len(split_om) - 1:
        break
x = 13
g = 0
b = 0
s = 0
for medal in split_om:
    x = x + 7
    y = y + 14
    medal_data = split_om[y]
    noc_data = split_om[x]
    #print(split_om[x])

    if medal_data == "Gold":
        if noc_dict[noc_data] =
        g = g + 1
        noc_dict[noc_data] = "Gold:" + str(g)

    """
    if noc_dict[noc_data] == "":
        if medal_data == "Gold":
            noc_dict[noc_data] = "Gold"
        if medal_data == "Bronze":
            noc_dict[noc_data] = "Bronze"
        if medal_data == "Silver":
            noc_dict[noc_data] = "Silver"
    """
    x = x + 7
#if noc_dict[noc_data] == None:



    if y == len(split_om) - 1:
        break
print(noc_dict)
print(medal_dict)
print(y)
#read the 6th space and add 1 to the NOC (like NOR)??








#transform data into something we can search
    #split data into lines and columns (so "\t" and "\n??")
    #want to read metal type and NOC
    #store it in a dictionary
#search number of medals assigned to NOC
