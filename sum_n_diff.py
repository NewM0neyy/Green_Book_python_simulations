import numpy as np
def uni(trials=100000):
  fav=0 #favrable event
  for _ in range(trials):
    x=np.random.uniform(0,1)
    y=np.random.uniform(0,1)
    if x+y>=2*np.abs(x-y):
      fav+=1
  return fav/trials
print(uni())



    
