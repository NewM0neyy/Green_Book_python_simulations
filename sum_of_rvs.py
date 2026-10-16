import numpy as np
import matplotlib.pyplot as plt
def uni(trials=100000,n=5):
  var=np.random.uniform(0,1,size=(trials,n))
  sum_less_1=np.sum(np.sum(var,axis=1)<=1)
  return sum_less_1/trials
n=np.arange(1,81)
prob=[uni(n=i) for i in n]
plt.figure(figsize=(10,6))
plt.plot(n,prob,color='red')
plt.xlabel("N")
plt.ylabel("Prob")
plt.show()
