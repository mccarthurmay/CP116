print("This program computes wind chill in Fahrenheit.")
#Prompt the user to input which city's data should be read.
#Found ANSI escape codes to bold text within an input on https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803.
filename = input("   Enter the name of the city you are interested in: \u001b[1m")
#Reset bold.
print("\u001b[0m")
#Read the file that was requested. ".txt" was added to locate file.
#Found .lower() funciton to prevent case sensitivity on https://thehelloworldprogram.com/python/python-string-methods/#:~:text=upper()%20and%20.,of%20the%20characters%20to%20lowercase.
file = open(filename.lower() + ".txt")
#Extract data from lines 1 and 2.
#Found ".readlines()" on https://www.guru99.com/python-file-readline.html.
ln1 = file.readlines(1)
ln2 = file.readlines(2)
#Convert extracted data into string. "t" = temperature and "ws" = windspeed.
#Found ".join()" function to convert a list to a string on https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output.
#Found ".strip()" function to remove the spacing (\n) on https://www.w3schools.com/python/ref_string_strip.asp#:~:text=The%20strip()%20method%20removes,any%20whitespaces%20will%20be%20removed.
t = ''.join(ln1).strip()
ws = ''.join(ln2).strip()
#Print the information from the city that was chosen.
print("When the temp is " + t + " F and the wind speed is " + ws +" MPH,")
#Calculate the wind chill in Fahrenheit.
wc = 35.74 + 0.6215 * float(t) - 35.75 * (float(ws)**0.16) + 0.4275 * float(t) * (float(ws)**0.16)
#Print the resulting wind chill, rounding to the nearest tenth.
print("    the wind chill in F is " + str(round(wc,1)) + ".")
