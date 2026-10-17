import numpy as np
import matplotlib.pyplot as plt
def uni(trials=100000,no_of_ants=500):
  max_time=[]
  for _ in range(trials):
    dist=np.random.uniform(0,1,size=no_of_ants)
    
    max_time.append(np.max(dist))
  return np.mean(max_time)
no_of_ants=np.arange(1,101)
max_t=[uni(no_of_ants=i) for i  in no_of_ants]
plt.figure(figsize=(10,5))
plt.plot(no_of_ants,max_t,color='red')

plt.xlabel("Number of ants")
plt.ylabel("Max time ")
plt.show()
  
