import numpy as np
import matplotlib.pyplot as plt
import math
 
def card_game(trials=100000):
  deck=np.repeat(np.arange(1,14),4)
  total_comb=math.comb(52,5)
  four_card=0
  hand_w_two=0
  full_house=0
  indices=np.random.randint(0,52,size=(trials,5))
  hands=deck[indices]
  for hand in hands:
    _,counts=np.unique(hand,return_counts=True)
    if 4 in counts:
      four_card+=1
    if 2 in counts:
      hand_w_two+=1
    if len(counts)==2 and 3 in counts:
      full_house+=1

    p_1=four_card/total_comb
    p_2=hand_w_two/total_comb
    p_3=full_house/total_comb

  print(f"Four Hand :{p_1}")
  print(f"Two :{p_2}")
  print(f"Full House: {p_3}")

  x_labels=["Full HOuse","Two Hand","Four Hand"]
  y_labels=[p_1,p_2,p_3]
  plt.bar(x_labels,y_labels)
  plt.show()

card_game()
    
  
      
    
    

  
    
