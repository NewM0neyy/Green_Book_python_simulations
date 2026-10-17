import numpy as np
import matplotlib.pyplot as plt
def uni_rv(trials=1000000,no_of_rv=2):
  output=np.random.uniform(0,1,size=(trials,no_of_rv))
  product = np.prod(output, axis=1)
  fav_output = np.where(product > 0.5, 1, 0)
  return np.sum(fav_output)/trials
no_of_rv=np.arange(1,6)
prob=[uni_rv(no_of_rv=i) for i in no_of_rv]
plt.plot(no_of_rv,prob,color='red')

plt.xlabel("No of rv's")
plt.ylabel("Prob of prod >1/2")
plt.show()
