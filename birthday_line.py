import numpy as np
import matplotlib.pyplot as plt
def birthday_line(n,trials=100000):
  date=np.random.randint(1,366,size=(trials,n))
  date.sort(axis=1)
  diff=np.diff(date,axis=1)
  count=np.any(diff==0,axis=1)
  return np.mean(count)
a=np.arange(1,81)
cum_prob = np.array([birthday_line(n) for n in a])
prob=np.diff(cum_prob,prepend=0)
plt.figure(figsize=(10,6))
plt.plot(a,prob,color='red')
plt.xlabel("Number of people present in line")
plt.ylabel("Prob of having same birthday")
plt.show()
        
  
  
  
