
import os

#add new function - line 41
#add filter - line 46
#use compact for loop - lines 43, 25,115,168,260

def main():

    action = "" #placeholder
    data = {}
    grade_dict = {}
    honor_roll_list = []
#   make sure directory exists for save/load https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
    try:
        os.makedirs("./class_number/")
    except FileExistsError:
        pass


#   print data function
    def print_data(data):
#       print key, print each value per key
        for key, value in data.items():

            print (key)
            [print(list(value)[i] + ":", list(value.values())[i]) for i in range(0,4)]
            #for i in range(0,4):
                #print(list(value)[i] + ":", list(value.values())[i]


#   add student function
    def add_student(data,name):

#       check if student already exists
        if name not in data:
#           create dictionary, {name:{day#:score}}
            data[name] = {"day0":0, "day1":0,"day2":0,"day3":0}
            return print("Student Added Successfully")

        else:
            return print("Error: Student already exists")
    #add grades to list
    def honor_roll(name):
        [honor_roll_list.append(data[name]["day"+str(i)]) for i in range (0,4)]
        return
    #filter for honor roll
    def honor_roll_test(x):
        if x > "90":
            return True
        else:
            return False

#   set score function
    def set_score(data, name, day, score):

#       check if student exists
        if name in data:

#           check if day follows format (0-3 days)
            if day in str([0,1,2,3]):
#               update previously used grade_dict with outdated student-specific information - - ran into problem where data gets overwritten
                grade_dict.update(data[name])
#               update temp-dictionary with information
                grade_dict["day" + day] = score
#               update student specific dictionary with temp-storage dictionary
                data[name].update(grade_dict)

                return print("Score Set")


            else:
                return print("Error: Not a valid 'day'")


        else:
            return print("Error: Student is not in registry.")



#   set all score function
    def set_all_scores(data, name, score):

#       check if student exists
        if name in data:

#           repeat 4 times, i being number of repeat
            for i in range(0,4):
#               update previously used grade_dict with outdated student-specific information - - ran into problem where data gets overwritten
                grade_dict.update(data[name])
#               update each day in temp-dictionary with input score
                grade_dict["day" + str(i)] = score
#               update student specific dictionary with temp-storage dictionary
                data[name].update(grade_dict)

            return print("All Scores Updated")

        else:
            return print("Error: Student is not in registry.")



#   get average score function
    def get_average_score(data, day):

#       check if dictionary is empty https://www.freecodecamp.org/news/how-to-check-if-a-list-is-empty-in-python/
        if not data:
            return

        else:
            try:
#               convert all keys to list of names (key = name)
                keys = list(data.keys())
                day_list = []

#               for each student, locate the day#, append score to day_list ({name, {day:1}})
                [day_list.append(int(data[key_name]["day"+day])) for key_name in keys]
                #for key_name in keys

                    #day_list.append(int(data[key_name]["day"+day])) #was having trouble reading nested dictionaries https://www.programiz.com/python-programming/nested-dictionary

#               average
                avg = sum(day_list) / len(day_list)
                return print("The average is", avg)
            except:
                return print("Day does not exist")


#   load file function
    def load_file(classroom):
        try:
#           navigate, open, read, and spkit file by \n
            open_file = open("./class_number/" + classroom + ".txt")
            contents = open_file.read()
            contents_split = contents.split("\n")
            num = 0

#           run this the [(total number of words) - 1]/5 times
            for i in range(int((len(contents_split) - 1)/5)):
                name = contents_split[num]
                day0 = contents_split[1 + num]
                day1 = contents_split[2 + num]
                day2 = contents_split[3 + num]
                day3 = contents_split[4 + num]
                num = num + 5

#               create dictionary if name is not already in dictionary
                if name not in data:
#                   inputs values previously defined into dictionary
                    data[name] = {"day0":day0, "day1":day1,"day2":day2,"day3":day3}

                    continue

            print("Students Added Successfully")
        except:
            print("Class not found")


#   save file function
    def save_file(classroom, data):

#       create file in "class_number" folder https://www.w3schools.com/python/python_file_write.asp
        class_file = open("./class_number/" + classroom + ".txt", "w")

#       loop for every key, value in data.items(). For every key, write the key in file and skip line
        for key, value in data.items():
            class_file.write(key + "\n")

#           for every key, write every score value for each day
            [class_file.write(str(list(value.values())[i]) + "\n") for i in range(0,4)]
            #for i in range(0,4):

                #class_file.write(str(list(value.values())[i]) + "\n"



#   print_help function
    def print_help(action):
        print("\t'add': Add a new student")
        print("\t'set': Update a student's score")
        print("\t'setall': Update all of a student's scores")
        print("\t'see': View all student's scores")
        print("\t'avg': Get the average score for an assignment")
        print("\t'quit': Exit the program")
        print("\t'load': Load previous student information")
        print("\t'save': Save all student information for later use")
        print("\t'honor': Days with a grade over 90")


#   prompts
    while action != "quit":

#       ask user for action input
        action = input("What action would you like to take? ('help' for options): \u001b[1m").strip().lower()
        print("\u001b[0m")

#       run print_help function
        if action == "help":
            print_help(action)

#       run load_file function
        elif action == "load":
            classroom = input("Class you would like to load: \u001b[1m")
            print("\u001b[0m")

            load_file(classroom)

#       run save_file function
        elif action == "save":
            classroom = input("Name of class: \u001b[1m")
            print("\u001b[0m")

            save_file(classroom, data)


#       run print_data function
        elif action == "see":

            print_data(data)

#       run add_student function
        elif action == "add":
            name = input("Student Name: \u001b[1m")
            print("\u001b[0m")

            add_student(data,name)

#       run set_score function
        elif action == "set":
            name = input("Student Name:  \u001b[1m")
            print("\u001b[0m")
            day = input("Day to edit:  \u001b[1m")
            print("\u001b[0m")
            score = input("Score:  \u001b[1m")
            print("\u001b[0m")

            set_score(data, name, day, score)

#       run set_all_scores function
        elif action == "setall":
            name = input("Student Name: \u001b[1m")
            print("\u001b[0m")
            score = input("Set All Scores: \u001b[1m")
            print("\u001b[0m")

            set_all_scores(data, name, score)

#       run get_average_score function
        elif action == "avg":
            day = input("Day to average: \u001b[1m")
            print("\u001b[0m")

            get_average_score(data, day)
        #run honor_roll function
        elif action == "honor":
            name = input("What student would you like to see: \u001b[1m")
            print("\u001b[0m")

            honor_roll(name)

            honor_roll_list = list(filter(honor_roll_test, honor_roll_list))
            [print("day" + str(i) + ":", honor_roll_list[i- 1]) for i in range(len(honor_roll_list))]

main()
