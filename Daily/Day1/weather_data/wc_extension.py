#As an extension, I allowed the user to supply the city name as a command line argument and added an option to automatically
#determine the measuring system the user is most likely using via a small prompt

import sys
#Found information on system arguments from https://www.pythonforbeginners.com/argv/more-fun-with-sys-argv.
#Calculate the length of system argument.
#If length = 2, then use the first argument as filename.
if len(sys.argv) == 2:
    filename = f"{sys.argv[1]}"
#If length = 3, then use the first and second argument as filename.
elif len(sys.argv) == 3:
    filename = f"{sys.argv[1]} {sys.argv[2]}"
#If there are no additional arguments, prompt user within program.
elif len(sys.argv) == 4:
    print("Too many arguments.")
    exit()
else:
    print("This program computes wind chill.")
    filename = input("Enter the name of the city you are interested in: \u001b[1m")
    print("\u001b[0m")
#Input determines if the Imperial or Metric system is being used. ".lower()" prevents case sensitivity.
sys = input("Are you from the U.S., Liberia, or Myanmar? (Yes or No) \u001b[1m").lower()
#Reset bold.
print("\u001b[0m")
#Read the file that was requested. ".txt" was added to locate file.
file = open(filename.lower() + ".txt")
#Extract data from lines 1 and 2 of specific txt file.
ln1 = file.readlines(1)
ln2 = file.readlines(2)
#Convert extracted data into string. ln1 is temperature and ws is windspeed.
t = float(''.join(ln1).strip())
ws = float(''.join(ln2).strip())
#If the user is not from an Imperial system based country, calculate data for Metric system.
if sys == "no":
    #Convert temperature to Celcius.
    t = (t - 32) * 5/9
    #Convert wind speed to KPH.
    ws = ws * 1.609344
    #Temperature label.
    tl = " C"
    #Speed Label.
    sl = " KPH"
    #Calculate wind chill.
    wc = 13.12 + 0.6215 * t - 11.37 * (ws**0.16) + 0.3965 * t * (ws**0.16)
if sys == "yes":
    wc = 35.74 + 0.6215 * t - 35.75 * (ws**0.16) + 0.4275 * t * (ws**0.16)
    tl = " F"
    sl = " MPH"
#Print the information from the city that was chosen.
print("When the temp is " + str(round(t,1)) + tl + " and the wind speed is " + str(round(ws,1)) + sl + ",")
#Print the resulting wind chill, rounding to the nearest tenth.
print("the wind chill is " + str(round(wc,1)) + tl + ".")
