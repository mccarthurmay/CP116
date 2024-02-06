import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#open olympic_medals as datafile
df = pd.read_csv("olympic_medals.tsv", delimiter="\t")
choice = ""


#Which countries have won the most medals?
    #a. This plot displays the medal count for the top 10 NOC with most medals.
    #b. It only has 4 main data ink: axes, axes labels, title, and data. The axes
        #and axes labels tell the user what they are looking at to answer the question
        #themselves. The title tells the user what the plot is trying to convey. The
        #plotted data allows the user to visualize a rough estimate of how many Medals
        #each country has.
    #c. I chose a simple bar plot because there is no need for extra information that may
        #confuse the user or provide too much information.
    #d. I could have used a scatter plot to recreate a dot plot, but this would have put an
        #excess amount of information that would be near impossible to grasp with medal counts
        #in the thousands.
def total_medals():
    noc_dict = {}
    #NOC and number of times it shows up
    medal_count = df["NOC"].value_counts()

    #{NOC: number of medals} for top 10 countries with most medals
    for i in range(0,10):
      noc_dict[medal_count.keys()[i]] = medal_count[i]

    #plot data
    p = sns.barplot(x = noc_dict.keys(),
                y = noc_dict.values(),
                data = noc_dict)
    p.set(title='Top 10 Countries with Most Medals',  xlabel="Country (NOC)", ylabel="Medal Count")
    plt.show()


#Which sports have the youngest athletes? The oldest? How much spread is there?
    #a. This shows which sports have the youngest/oldest athletes.
    #b. There are a few different parts of data ink. The axes serve to give the user data
        #so they can deduce what is happening. The title also serves a similar purpose.
        #For the data, the box and whisker plots give the user 9 things: outliers, minimum
        #age, max age, 25th percentile, median, 75th percentile, IQR, and spread.
    #c. Box and whisker plots are known to give immense amounts of data that can aid in
        #accurately make conclusions. For instance, the presence of outliers can show the
        #user that an all-time high or low age is not normal.
    #d. I could have used a violin plot, but I found that the density plot seemed redundant
        #if we're focusing on spread, min, and max of ages. The box and whisker plot
        #gives all the same information besides frequency, which was not needed for this task.
def athletes():
    type_yo = ""
    sport_dict = {}
    age_li = []
    sport_col = df["Sport"]
    age_col = df["Age"]

    #put every sport into a dictionary with a list of ages that played the sport
    for i in range(len(sport_col)):

        sport = sport_col[i]
        age = age_col[i]
        #if sport doesn't have a dictionary, make one with an empty list
        if sport not in sport_dict:
            sport_dict[sport] = []
        #only append indexes with ages that exist
        if not pd.isna(age):
            sport_dict[sport].append(age)


    sport_name = df[["Sport", "Age"]]
    #remove NaN
    sport_name = sport_name.dropna(subset=['Age'])
    #sort by Age
    sport_name = sport_name.sort_values(by=['Age'])
    #remove duplicate sport names, keeping the ones with the lowest/highest age
    sport_name_y = sport_name.drop_duplicates(subset = 'Sport', keep = 'first').reset_index(drop=True)
    sport_name_o = sport_name.drop_duplicates(subset = 'Sport', keep = 'last').iloc[::-1].reset_index(drop=True)

    #append 10 youngest sports to list
    young_sport = []
    for i in range(0,10):
        young_sport.append(sport_name_y['Sport'][i])

    #append 10 oldest sports to list
    old_sport = []
    for i in range(0,10):
        old_sport.append(sport_name_o['Sport'][i])

    #only keep sport names in top 10 youngest/oldest
    def exists_y(key):
        return key in young_sport
    def exists_o(key):
        return key in old_sport
    sport_data_y = {key: sport_dict[key] for key in filter(exists_y, sport_name_y['Sport'])}
    sport_data_o = {key: sport_dict[key] for key in filter(exists_o, sport_name_o['Sport'])}

    #turn dictionaries into indicies so matplot can read it
    sport_data_y = pd.DataFrame.from_dict(sport_data_y, orient = 'index') #https://stackoverflow.com/questions/61255750/convert-dictionary-of-dictionaries-using-its-key-as-index-in-pandas
    sport_data_o = pd.DataFrame.from_dict(sport_data_o, orient = 'index')

    def plot_young():
        plt.subplots(figsize=(12,8))
        sns.boxplot(data = sport_data_y.T).set(title='10 Sports with Youngest Athletes',  xlabel="Sport", ylabel="Ages")
        plt.xticks(rotation=45)
        plt.show()
    def plot_old():
        plt.subplots(figsize=(12,8))
        sns.boxplot(data = sport_data_o.T).set(title='10 Sports with Oldest Athletes',  xlabel="Sport", ylabel="Ages")
        plt.xticks(rotation=45)
        plt.show()

    #commands
    while type_yo != "quit":
        type_yo = input("Show plot for athlete ages (young, old): ")
        if type_yo == 'young':
            plot_young()
        elif type_yo == 'old':
            plot_old()



#Does athlete height have any relationship to other attributes of the athletes? If so, which ones?
    #I found that using several different plots would make comparisons more accurate.
    #age:
        #a. I used a scatter plot to show that there is little correlation between height
            #and age.
        #b. The labels and title convey what the user is looking at. The scatter points
            #are placed to show that as age increases, height tends not to increase.
        #c. I chose a scatter plot to be able to plot all data possible without anything being
            #too complicated. It shows a high density of age and how the height does not increase
            #or decrease as age increase.
        #d. I could have done a line graph comparing the averages or added a linear regression
            #line, but after trying that I noticed that the lack of data near the older side led
            #to skewed data. This had the line begin decreasing after the age of about 40. So, I left
            #the graph at a scatter plot.
    #weight:
        #a. I used a joint plot to show that as height increases, weight also increases.
        #b. The labels and title convey what the user is looking at. The scatter Points
            #are two different colors to show M and F. The frequency plots on the x and y axis
            #shows how the data is distributed between M and F.
        #c. I found that the added distributions of data on the axis helps the user understand
            #where the mean weight and heights are while seing that as heigh tincreases, weight
            #also increases.
        #d. A simple scatter plot could have been used to show the relationship between Weight
            #and height, but the introduction of distributions allows the user to see where the
            #outliers are likely to be, as these are all roughly normal.
    #sport:
        #a. I used a box and whisker plot to show the correlation between height and sport.
        #b. Each box and whisketr plot gives the ability to draw important conclusions,
            #including how important height actually is to the sport. A box and whisker with
            #a massive spread that goes through a wide range of heights may suggest that height
            #is not a proponent of the sport. A sport with a high maximum, such as basketball,
            #may suggest that height is important.
        #c. I mainly wanted to see the median height for each sport, which also tells the user
            #if height may be a benefit in the sport.
        #d. I could not think of using any other plot to sum up so many sports without going
            #though each one wiht a scatter plot. This may have been more detailed, but it would
            #have been a much larger pain for both the user and I. Box and whisker plots give a
            #good summary. 
def height():
    type = ""

    def plot_data(type):
        #plot age
        if type == "age":
            p =sns.relplot(
                data = df,
                y="Height",
                x="Age",
                col = "Sex",
                kind = "scatter",
                hue = "Sex"
            )

            p.set(ylabel = "Height(cm)")
            p.fig.suptitle("Comparison of Height vs Age")
            plt.show()
        #plot weight
        if type == "weight":
            p = sns.jointplot(
                data = df,
                x="Height",
                y="Weight",
                kind = "scatter",
                hue = "Sex",
                s = 20
            )

            p.set_axis_labels("Height(cm)", "Weight")
            p.fig.suptitle("Comparison of Height vs Weight")
            plt.show()

        #plot sport
        if type == "sport":
            plt.subplots(figsize=(16,10))
            sns.set(font_scale=.75)
            p = sns.boxplot(
                data = df,
                y="Height",
                x="Sport"
            )
            p.set(title = "Comaprison of Height vs Sport", xlabel = "Height(cm)")
            #rotate ticks to make more visible
            plt.xticks(rotation=75)
            plt.show()

    #actions for user
    while type != "quit":
        type = input("What would you like to compare (age, weight, sport): ")
        plot_data(type)



while choice != "quit":
    print("What would you like to see?")
    print("\tWhich countries have the most medals? (1)")
    print("\tWhich sports have the youngest athletes? The oldest? (2)")
    print("\tDoes athlete height have any relationship to other attributes of the athletes? (3)")
    print("Typing 'quit' at any instance will bring you back a menu.")
    choice = input("Choose: ")
    if choice == "1":
        total_medals()
    elif choice == "2":
        athletes()
    elif choice == "3":
        height()
