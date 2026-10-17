import numpy as np
import matplotlib.pyplot as plt
def flip(trials=100000,no_of_coins=4):
  initial_flip=np.random.randint(0,2,size=(trials,no_of_coins))
  initial_head=np.sum(initial_flip,axis=1)
  second_flips=np.random.randint(0,2,size=(trials,no_of_coins))
  second_head=np.sum(second_flips,axis=1)
  payout=np.where(initial_head<=1,second_head-1,initial_head)
  return np.mean(payout)
no_of_coin=np.arange(1,11)
payoff=[flip(no_of_coins=i) for i in no_of_coin]
plt.figure(figsize=(10,6))
plt.plot(no_of_coin,payoff,color='green')
plt.xlabel("No of coins")
plt.ylabel("Payoff")
plt.show()


  
    
    
