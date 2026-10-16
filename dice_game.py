import numpy as np
def rollin(trials=100000):
  payoffs=np.zeros(trials)
  for t in range(trials):
    payoff=0
    while True:
      roll=np.random.randint(1,7)
      payoff+=roll
        
      if roll in [1,2,3]:
        break
    payoffs[t]=payoff
  return np.mean(payoffs)
print(rollin())

        
        
