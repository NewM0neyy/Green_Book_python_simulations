import numpy as np
import matplotlib.pyplot as plt
def wrong_firms(n=5,trials=100000):
  letter=np.arange(1,n+1)
  correct_counts=[]
  for _ in range(trials):
    l=np.random.permutation(letter)
    correct_counts.append(np.sum(l==letter))
  
  val,counts=np.unique(correct_counts,return_counts=True)
  prob=counts/trials
  plt.bar(val,prob,color='red')
  plt.xlabel("Number of correct envelopes")
  plt.ylabel("Prob")
  plt.show()

wrong_firms()
