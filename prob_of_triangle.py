import numpy as np
def uni(trials=100000):
  cuts=np.random.uniform(0,1,size=(trials,2))
  cuts.sort(axis=1)
  x=cuts[:,0]
  y=cuts[:,1]
  l1=x
  l2=y-x
  l3=1-y
  cond=(l1+l2>l3) & (l2+l3>l1) & (l3+l1>l2)
  return np.mean(cond)
print(uni())
      
  
