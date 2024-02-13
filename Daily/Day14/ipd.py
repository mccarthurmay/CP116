from random import choice,shuffle,random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# How much each outcome is worth.
# Note that 0 is also an option.

#Extension: tried a more complicated experiment, changed the population to 1/3 CommonTitForTat
LOSE = 10
WIN = 50
TIE = 30

# The basic Agent class.
class Agent():

    # initialize an agent with no scores or memory.
    def __init__(self):

        self.scores = []
        self.history = []

    # return this agent's average score.
    def mean_score(self):
        return sum(self.scores)/len(self.scores)

    # reset this agent's memory.
    def reset(self):
        self.history=[]

    def __str__(self):
        return "I'm an agent!"


class CollabAgent(Agent):

    def get_choice(self, other_hist):
        return "C"

    def __str__(self):
        return "collab"

class DefectAgent(Agent):

    def get_choice(self, other_hist):
        return "D"

    def __str__(self):
        return "defect"


class TrustingTitForTatAgent(Agent):

    def get_choice(self, other_hist):
        if len(other_hist) == 0:
            return "C"
        else:
            return other_hist[-1]
    def __str__(self):
        return "TTFT"
class CommonTitForTatAgent(Agent):

    def get_choice(self,other_hist):
        if other_hist.count("D") > other_hist.count("C"):
            return "D"
        else:
            return "C"
    def __str__(self):
        return "CTFT"

class ProbMaxAgent(Agent):

    def get_choice(self,other_hist):
        if len(other_hist) == 0:
            return "C"
        else:
            prob_other_defects = other_hist.count("D")/len(other_hist)
            prob_other_collabs = other_hist.count("C")/len(other_hist)

            score_if_defect = prob_other_collabs*WIN
            score_if_collab = prob_other_collabs*TIE + prob_other_defects*LOSE

            if score_if_collab >= score_if_defect:
                return "C"
            else:
                return "D"
    def __str__(self):
        return "probmax"
def versus(agent_A, agent_B):
    # Play many games against each other.
    for i in range(300):
        # get agent A's choice, which can use its knowledge of how B has played so far.
        choiceA = agent_A.get_choice(agent_B.history)
        # get agent B's choice, which can use its knowledge of how A has played so far.
        choiceB = agent_B.get_choice(agent_A.history)

        # append both choices to that player's history.
        agent_A.history.append(choiceA)
        agent_B.history.append(choiceB)

        # based on who chose what, assign points.
        if choiceA == "D" and choiceB == "D":
            agent_A.scores.append(LOSE)
            agent_B.scores.append(LOSE)
        elif choiceA == "C" and choiceB == "D":
            agent_A.scores.append(0)
            agent_B.scores.append(WIN)
        elif choiceA == "D" and choiceB == "C":
            agent_A.scores.append(WIN)
            agent_B.scores.append(0)
        elif choiceA == "C" and choiceB == "C":
            agent_A.scores.append(TIE)
            agent_B.scores.append(TIE)

# A list of all the subtypes of Agent.
# Note that these are the type names, NOT instances!
agent_types = [
               CollabAgent,
               DefectAgent,
               TrustingTitForTatAgent,
               CommonTitForTatAgent,
               ProbMaxAgent]

# Making a random population of lots of agents.

#Adjusted the population for 100 CTFT
population = [CommonTitForTatAgent() if i < 100 else choice(agent_types)() for i in range(300)]
#(removed random)
#Collab Scores: Scores became much more 'linear' as CTFT was more prevelant.
#CTFT Scores: Scores were much higher on average, being able to counter defect and collab with collab much more often.
#Defect scores: Saw a long line of an average score of ~17.8, likely due to a high number of rounds with CTFT in those games
#probmax scores: On average, lower than usual. It can't predict what CTFT would do if CTFT plays based on agent.
#TTFT scores: the averages were much higher as most of these agents were ones to tie, and the averages of 30 show that TTFT never saw a defect agent

#Conclusion: The better option is forgiveness, mainly going for the tie. We see that most agents are willing to tie, and some rounds may not even see
#the one agent that defects. 


# Ten rounds of playing agents against each other
for i in range(10):
    #shuffle the entire population
    shuffle(population)

    # reset all of the agents' memories.
    for agent in population:
        agent.reset()

    # loop through the shuffled population two at a time,
    # and play agents against each other.
    for j in range(0,len(population),2):
        A = population[j]
        B = population[j+1]

        versus(A,B)

# make an empty dict to hold all of the agents
agents_by_type = {item:[] for item in agent_types}
scores = [agent.mean_score() for agent in population]
types = [str(agent) for agent in population]

df = pd.DataFrame({"Scores": scores, "Type":types})
type_list = []
name_list = []
type_dict = {}


for agent_type in df['Type'].unique():
    #create dictionary for each agent name with their respective points
    type_dict[agent_type] = list(df.loc[df['Type'] == agent_type, 'Scores'])
    #create list of names for plot title
    name_list.append(agent_type)
    #create list containing all scores in correspondance to plot title
    scores_list = list(df.loc[df['Type'] == agent_type, 'Scores'])
    num_scores = len(scores_list)
    type_list.append(list(range(num_scores)))

#plot every agent separately
for i in range(0,5):
    sns.scatterplot ( x = type_list[i], y = list(type_dict.values())[i]) #scatter?
    plt.title(f"{name_list[i]}: Scores By Round")
    plt.xlabel("Round Number")
    plt.ylabel("Average Points Won Per Round")
    plt.show()


for agent in population:
    agents_by_type[type(agent)].append(agent)

for a_type in agents_by_type:
    agents = agents_by_type[a_type]
    print(a_type, sum([a.mean_score() for a in agents])/len(agents))
