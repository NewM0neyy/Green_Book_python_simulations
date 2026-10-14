import random
import matplotlib.pyplot as plt
def gamblin(n,p,trials,starting_cap):
  ruin=0
  success=0
  total_rounds=0
  for _ in range(trials):
    current_cap=starting_cap
    while 0<current_cap<n:
      if random.random()<p: # p is winning probability
        current_cap+=1
      else:
        current_cap-=1
      total_rounds+=1
    if current_cap==0:
      ruin+=1
    else:
      success+=1
  prob_of_ruin=ruin/trials
  prob_of_winning=success/trials
  return prob_of_winning
n=[6,7,8,9]
p=0.5
prob=[gamblin(n=i,p=p,trials=100000,starting_cap=1) for i in n ]
plt.figure(figsize=(10,6))
plt.plot(n,prob,color='red')
plt.xlabel("cashing out at N")
plt.ylabel("prob of winning")
plt.show()
