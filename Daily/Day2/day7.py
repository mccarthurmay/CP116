import re
import sys

#Open and parse the data to compute the medal counts for all NOC codes
file = open("olympic_medals.tsv")
om = file.read()
print("This program counts the olympic medals won by different countries.")

#Prompt the user for a NOC of interest
try:
    noc = sys.argv[1]
except:
    noc = input("Input desired NOS: \u001b[1m").upper()
print("\u001b[0m")

#import sys - line 10, allows first system argument to be the input
#filter - line 24/33, prints filters noc and filters gold/silver/bronze


#split "om" into lines and columns
#using re.split() to split with two separators - had trouble splitting more than once with .split() https://pynative.com/python-regex-split/
split_om = re.split(r"\t|\n", om)


#create an empty dictionary for NOC
noc_dict = {}
#create key based off input with empty value
noc_dict[noc] = ""


def has_noc(n):
    noc_word = [noc]
    if n in noc_word:
        return True
    else:
        return False

noc_medals = len(list(filter(has_noc, split_om)))

def total_medals(x):
    medals_word = ["Gold", "Silver", "Bronze"]
    if x in medals_word:
        return True
    else:
        return False

total_medals = len(list(filter(total_medals, split_om)))

#the location of the first medal/noc
noc_location = 20
medal_location = 27
#set the count of each medal to 0
gold_list = []
silver_list = []
bronze_list = []

#loop, make a key for each NOC, add value of number of medals
for data in split_om:
    #define noc_data as current NOC being read
    noc_data = split_om[noc_location]
    #define medal_data as current medal being read
    medal_data = split_om[medal_location]

    #if the user input matches the noc being read, begin counting medals
    if noc_data == noc:
        #add medal count to respective medal tiers
        if medal_data == "Gold":
            gold_list.append(medal_data)

        elif medal_data == "Silver":
            silver_list.append(medal_data)

        elif medal_data == "Bronze":
            bronze_list.append(medal_data)

    #break code when the last NOC and Medal are counted
    if noc_location == len(split_om) - 8:
        break

    #location of noc relative to number of split. Located on the 14th split after the last location.
    noc_location = noc_location + 14
    #location of medal relative to number of split. Located on the 14th split after the last location.
    medal_location = medal_location + 14




#add medal counts to key
noc_dict[noc] = "\n Gold: " + str(len(gold_list)) + "\n Silver: " + str(len(silver_list)) + "\n Bronze: " + str(len(bronze_list))
print("Total number of medals for", noc, noc_medals)
print("fun fact: total medals for all noc", total_medals)
#print dictionary
print("The total medal counts for", noc, "are:", noc_dict[noc])