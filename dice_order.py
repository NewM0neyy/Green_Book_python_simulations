import numpy as np
def rollin(trials=100000):
  d1=np.random.randint(1,7,size=trials)
  d2=np.random.randint(1,7,size=trials)
  d3=np.random.randint(1,7,size=trials)
  fav = (d1 < d2) & (d2 < d3)
  prob=np.mean(fav)
  return prob
print(rollin())


   
  
