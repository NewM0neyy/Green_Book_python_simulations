import numpy as np
import random
def unfair_coin(trials=100000,no_of_toss=10):
  unfair=['H','H']
  fair=['H','T']
  coin_chosen=[unfair]*1+[fair]*99
  
  all_head=0
  head_w_unfair_coin=0
  for _ in range(trials):
    head=0
    current_coin=random.choice(coin_chosen)
    for _ in range(no_of_toss):
      toss=random.choice(current_coin)
      if toss=='H':
        head+=1
    if head==no_of_toss :
        all_head+=1
        if current_coin==unfair:
          head_w_unfair_coin+=1
  return head_w_unfair_coin/all_head
print(unfair_coin())


    
        
  
