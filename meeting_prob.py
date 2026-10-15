import numpy as np
def meet(trials=100000):
  bankers_meet=0
  for _ in range(trials):
    
    banker_A=np.random.uniform(0,60)
    banker_B=np.random.uniform(0,60)
    if np.abs(banker_A-banker_B)<=5:
      bankers_meet+=1
  return bankers_meet/trials
print(meet())
  
  
