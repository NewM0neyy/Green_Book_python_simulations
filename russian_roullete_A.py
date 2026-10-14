import numpy as np
import matplotlib.pyplot as plt

def trigger(trials=100000):
  player1_loses=0
  player2_loses=0
  for _ in range(trials):
    roll=np.random.randint(1,7)
    if roll in [1,3,5]:
      player1_loses+=1
    if roll in [2,4,6]:
      player2_loses+=1
  p_1=player1_loses/trials
  p_2=player2_loses/trials
  x=["player 1 loses","player 2 loses"]
  y=[p_1,p_2]
  plt.figure(figsize=(10,6))
  plt.bar(x,y)
  plt.show()
trigger()
    
  
