import numpy as np
def trigger(trials=100000):
  player_1=0 #player 1 loses
  player_2=0 # player 2 loses
  for _ in range(trials):
    count=1

    while True:
      
      roll=np.random.randint(1,7)
      if  roll==1 and count%2!=0:
        player_1+=1
        break
      if roll==1 and count%2==0:
        player_2+=1
        break
      count+=1
  p_1=player_1/trials
  p_2=player_2/trials
  x=["player 1 loses","player 2 loses"]
  y=[p_1,p_2]
  plt.figure(figsize=(10,6))
  plt.bar(x,y)
  plt.show()
trigger()

  
        
        
    
