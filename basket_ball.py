import numpy as np
def baskets(trials=100000,throws=100):
  baskets=np.ones(trials,dtype=int)
  for i in range(3,throws+1):
    p=baskets/(i-1)
    random=np.random.rand(trials)
    baskets+=(random<p).astype(int)
  count_50=np.sum(baskets==50)
  prob=count_50/trials
  return prob
print(baskets())
  
