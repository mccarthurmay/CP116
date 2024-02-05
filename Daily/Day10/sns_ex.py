import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("olympic_medals.tsv", delimiter="\t")

#using pandas

#create list of every noc
#count = df[noc].value_counts()[noc_name]
#{CHN: 1, USA: 5, KOR: 20} set value of each 
"""
selection = df[(df["NOC"] == "AUS") | (df["NOC"] == "USA")]


# Seaborn theme
sns.set_theme(style="whitegrid")

sns.scatterplot(
    data = selection,
    y="NOC", x="Medal"

)
#amt of athelets
plt.show()
"""
