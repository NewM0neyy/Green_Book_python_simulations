import numpy as np
import matplotlib.pyplot as plt
def havin_same_birthday(trials=100000,n=5):
  birthdays=np.random.randint(1,366,size=(trials,n))
  same_bday=0
  for b in birthdays:
    if len(np.unique(b))==n-1:
      same_bday+=1
  prob=same_bday/trials
  return prob
n=list(range(1,81))
prob=[havin_same_birthday(n=i) for i in n]
plt.figure(figsize=(10,6))
plt.plot(n,prob,color='red',linewidth=2)
plt.show()
