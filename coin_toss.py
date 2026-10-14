import numpy as np
def toss(trials=100000):
  toss=['H','T']
  alice_win=0
  bob_win=0
  for _ in range(trials):
    t=""
    while True:
      
      alice=np.random.choice(toss)
      t+=alice
      if len(t)>=2 and t[-2:]=='HT':
        alice_win+=1
        break
      bob=np.random.choice(toss)
      t+=bob
      if len(t)>=2 and t[-2:]=='HT':
        bob_win+=1
        break
  p_a=alice_win/trials
  p_b=bob_win/trials
  return p_a
    
print(f"probability of alice winning is {toss()}")
  
      
      
  
