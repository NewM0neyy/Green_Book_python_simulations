import numpy as np
def draw(trials=100000):
  deck=np.array([1]*4+[0]*48)
  all_ace=0
  for _ in range(trials):
    shuffle=np.random.permutation(deck)
    p_1=shuffle[:13]
    p_2=shuffle[13:26]
    p_3=shuffle[26:39]
    p_4=shuffle[39:52]
    if np.sum(p_1)==1 and np.sum(p_2)==1 and np.sum(p_3)==1 and np.sum(p_4)==1:
      all_ace+=1
  p=all_ace/trials
  return p
print(draw())  
  
    
    
  
  
