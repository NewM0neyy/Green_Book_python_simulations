import numpy as np
def noodles(trials=100000,noodles=100):
  total_loops=0
  ends=np.repeat(np.arange(noodles),2)
  for _ in range(trials):
     loops=0
     shuffled=np.random.permutation(ends)
     pairs=shuffled.reshape(-1,2)
    # amkes 2 clos and n number of rows the n is calculated by numpy itself when u type -1
     groups=np.arange(noodles)
     for end1,end2 in pairs:
      g1=groups[end1]
      g2=groups[end2]
      if g1==g2:
        loops+=1
      else:
        groups[groups==g2]=g1
     total_loops+=loops  
        
  p=total_loops/trials
  return p
print(noodles())
    
