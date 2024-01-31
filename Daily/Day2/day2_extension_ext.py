#added an option to request additional data, drawing the age of the youngest and oldest medal winners, along with their age, name, year accomplished, sport, and medal awarded.
#calculated and provided information on the average age of atheletes awarded a medal_location

import re


#Open and parse the data to compute the medal counts for all NOC codes.
file = open("olympic_medals.tsv")
om = file.read()
print("This program counts the olympic medals won by different countries.")


#Prompt the user for a NOC of interest.
noc = input("Input desired NOS: \u001b[1m").upper()
print("\u001b[0m")
#Prompt the user if they would like additional information.
info = input("Would you like to know additional information on the atheles? (Yes or No) \u001b[1m").lower()
print("\u001b[0m")


#split "om" into lines and columns.
#using re.split() to split with two separators - had trouble splitting more than once with .split(). https://pynative.com/python-regex-split/
split_om = re.split(r"\t|\n", om)


#create an empty dictionary for NOC.
noc_dict = {}
#create an empty list for ages
age_list = []
#create key based off input with empty value.
noc_dict[noc] = ""



#the location of the first medal/noc/age/name/sport/year.
noc_location = 20
medal_location = 27
age_location = 16
name_location = 14
sport_location = 25
year_location = 22

#set count of total age.
total_age = 0

#set the count of each medal.
gold_count = 0
silver_count = 0
bronze_count = 0

#set empty variables for later use
young_name = ""
old_name = ""

#set count of total number of requested NOC.
total_noc = 0


#loop, make a key for each NOC, add value of number of medals
for data in split_om:
#define noc_data as current NOC being read
noc_data = split_om[noc_location]
#define medal_data as current medal being read
medal_data = split_om[medal_location]
#define age_data as current age being read
age_data = split_om[age_location]
#define name_data as current name being read
name_data = split_om[name_location]
#define sport_data as current sport being read
sport_data = split_om[sport_location]
#define year_data as current year being read
year_data = split_om[year_location]


#if the user input matches the noc being read, begin counting medals
if noc_data == noc:
    #add medal count to respective medal tiers
    if medal_data == "Gold":
        gold_count = gold_count + 1

    elif medal_data == "Silver":
        silver_count = silver_count + 1

    else:
        bronze_count = bronze_count + 1


    #make sure age data exists (found problems with setting age data as integer, determined that some may not exist)
    if age_data != "":
        #calculate total age and total accounts of recorded age for later calculation
        total_age = total_age + int(age_data)
        total_noc = total_noc + 1

        #second input on information
        if info == "yes":
            #add current age data if prompt was answered "yes" (and if age exists)
            age_list.append(age_data)
            #sort from smallest year to largest
            age_list.sort()

            #if the age added to the list is now the lowest age, then this is the new youngest athelete
            if age_list[0] == age_data:
                young_name = name_data
                young_medal = medal_data
                young_sport = sport_data
                young_year = year_data

            #if the age added to the list is now the highest age, then this is the new oldest athelete
            if age_list[-1] == age_data:
                old_name = name_data
                old_medal = medal_data
                old_sport = sport_data
                old_year = year_data

#break code when the last NOC and Medal are counted
if noc_location == len(split_om) - 8:
    break

#location of noc relative to number of split. Located on the 14th split after the last location.
noc_location = noc_location + 14
#location of medal relative to number of split. Located on the 14th split after the last location.
medal_location = medal_location + 14
#location of age relative to number of split. Located on the 14th split after the last location.
age_location = age_location + 14
#location of name relative to number of split. Located on the 14th split after the last location.
name_location = name_location + 14
#location of sport relative to number of split. Located on the 14th split after the last location.
sport_location = sport_location + 14
#location of year relative to number of split. Located on the 14th split after the last location.
year_location = year_location + 14



#add medal counts to key
noc_dict[noc] = "\n Gold: " + str(gold_count) + "\n Silver: " + str(silver_count) + "\n Bronze: " + str(bronze_count)

#print dictionary
print("The total medal counts for", noc, "are:", noc_dict[noc])

#print athlete information
if info == "yes":
print("The average age of athletes awarded a medal is", round(total_age/total_noc, 1), "years old.")
print("\nThe youngest athelete was named", young_name, "at", age_list[0], "years old in", young_year + ". He recieved a", young_medal, "medal in", young_sport + ".", "\nThe oldest athelete was named", old_name, "at", age_list[-1], "years old in", old_year + ". He recieved a", old_medal, "medal in", old_sport + ".")

input_noc = input("Tell me a NOC to look up")
