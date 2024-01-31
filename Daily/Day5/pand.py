import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("olympic_medals.tsv", delimiter="\t")  #delimiter stops it from requiring commas

#print(data)
#print(data["NOC"] == "FIN") #looks for column NOC, not including "NOC", says if FIN is true or not

#filter = data["NOC"] == "FIN" # new dataframe

#print(data[filter]) #now, only give me rows where the statement above is True
#print(data[filter]["Height"]) #filters by column named height
#print(data[filter]["Height"].mean()) #gives the mean
#print(data[filter][["Height","NOC"]])




nocs = ["NOC"]
nocs = list(set(nocs))

heights = []
medal_count = []

for noc in nocs:
    filter = data["NOC"] == noc
    height = data[filter]["Height"].mean()
    heights.append(height)
    medal_count.append(len(data[filter]))

print(heights)
print(medal_count)

plt.scatter(heights, medal_count)
plt.show()
