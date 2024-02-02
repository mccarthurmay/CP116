import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("olympic_medals.tsv", delimiter="\t")


selection = df[(df["NOC"] == "AUS") | (df["NOC"] == "USA")]
# Seaborn theme
sns.set_theme(style="whitegrid")

sns.catplot(
    data = selection,
    x="Season", y="Weight", col="NOC", hue="Sex", kind ="violin", dodge=True, cut=0, bw=.5

)
#amt of athelets
plt.show()
