import numpy as np
def rollin(trials=100000):
  total_payoff=0
  for _ in range(trials):
    game_payoff=0
    while True:
      roll=np.random.randint(1,7)
      if roll in [1,2,3]:
        game_payoff+=1
      elif roll in [4,5]:
        total_payoff+=game_payoff
        break
      elif roll==6:
        
        break
  expected_payoff=total_payoff/trials
  return expected_payoff
print(rollin()) 

      
         
