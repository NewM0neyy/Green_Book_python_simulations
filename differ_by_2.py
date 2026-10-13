import numpy as np
def rollin_die(trials=100000):
  die=np.arange(1,7)
  rolls=[]
  for _ in range(trials):
    expected_rolls=0
    while True:
      first_roll=np.random.choice(die)
      sec_roll=np.random.choice(die)
      expected_rolls+=1
      if np.abs(first_roll-sec_roll)==2:
        break
    rolls.append(expected_rolls)
  return np.mean(rolls)
  
print(rollin_die())
      
