import random
import numpy as np
import matplotlib.pyplot as plt
def prob_of_A_winnin(n,trials):
  # generating random toss
  toss_A=np.random.randint(0,2,size=(trials,n+1))
  toss_B=np.random.randint(0,2,size=(trials,n))
  # counting total heads
  heads_A=np.sum(toss_A,axis=1)
  heads_B=np.sum(toss_B,axis=1)
  # prob check
  a_win=heads_A>heads_B
  final_prob=np.mean(a_win)
  print(f"The final prob of A winning {final_prob})
  #plotting B'S distribution (n coins)
  fig,(ax1,ax2)=plt.subplots(1,2,figsize=(14,5))
  ax1.hist(heads_B,bins=np.arange(0,n+1)-0.5,rwidth=0.8,color='blue')
  ax1.set_title("Gambler B")
  ax1.set_xlabel("Number Of Heads")
  ax1.set_ylabel("Nmber of Trials")
  ax1.set_xticks(range(0,n+1))

  # plotting A'S distribution 
  ax2.hist(heads_A,bins=np.arange(0,n+2)-0.5,rwidth=0.8,color='red')
  ax2.set_title("Gambler A")
  ax2.set_xlabel("Number of heads")
  ax2.set_ylabel("Number of Trials")
  ax2.set_xticks(range(0,n+2))
  plt.tight_layout()
  plt.show()

def main():
  prob_of_A_winnin(10,5000)

main()
  
  
  
  
  
    
  
    
    
    
