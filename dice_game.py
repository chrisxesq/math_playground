from itertools import product
#First Task: Compare Two Dices 
#Implement a function that takes two dices as input and computes two values: the first value is the number of times the first dice wins (out of all possible 36 choices), the second value is the number of times the second dice wins. We say that a dice wins if the number on it is greater than the number on the other dice.

def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for p in product(dice1,dice2):
      if p[0]>p[1]:
        dice1_wins += 1
      elif p[0]<p[1]:
        dice2_wins += 1
    return (dice1_wins, dice2_wins)
  
#Second Task: Is there the Best Dice?
#Now, your goal is to check whether among the three given dices there is one that is better than the remaining two dices.
#Implement a function that takes a list of dices and checks whether there is dice (in this list) that is better than all other dices. We say that a dice is better than another one, if it wins more frequently (that is, out of all 36 possibilities, it wins in aaa cases, while the second one wins in bbb cases, and a>ba>ba>b). If there is such a dice, return its (0-based) index. Otherwise, return -1.

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    adj=[[]for _ in range(len(dices))]
    for i in range(len(dices)-1):
      for j in range(i+1,len(dices)):
        a,b=count_wins(dices[i],dices[j])
        print('ij',i,j,'ab',a,b)
        if a<b:
          adj[i].append(j)
        elif a>b:
          adj[j].append(i)
        else:
          adj[j].append(i)
          adj[i].append(j)
    ans=-1 
    for i in range(len(adj)):
      if len(adj[i])==0:
        ans=i
    return ans,adj

#Third Task: Implement a Strategy
#You are now ready to play!
#Implement a function that takes a list of dices (possibly more than three) and returns a strategy. The strategy is a dictionary:
#If, after analyzing the given list of dices, you decide to choose a dice first, set strategy["choose_first"] to True and set strategy["first_dice"] to be the (0-based) index of the dice you would like to choose
#If you would like to be the second one to choose a dice, set strategy["choose_first"] to False. Then, specify, for each dice that your opponent may take, the dice that you would take in return. Namely, for each i from 0 to len(dices)-1, set strategy[i] to an index j of the dice that you would take if the opponent takes the i-th dice first.

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)
    ans,adj=find_the_best_dice(dices)
    print(ans,adj)
    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    if ans!=-1:
      strategy["first_dice"] = ans
    else:
      strategy.pop("first_dice")
      strategy["choose_first"] = False
      for i in range(len(dices)):
        for k in adj[i]:
          a,b=count_wins(dices[i],dices[k])
          if a!=b:
            strategy[i]=k
            break
    return strategy
