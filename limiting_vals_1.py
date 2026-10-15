import numpy as np
def rollin(trials=100000):
  fair_val=[]
  for _ in range(trials):
    last_roll=0
    while True:
      
      roll=np.random.randint(1,7)
      last_roll=roll
      if roll==1:
        
        break
      fair_val.append(last_roll)
      
      
  p=np.mean(fair_val)
  return p
print(rollin())    
        
    
        
    
