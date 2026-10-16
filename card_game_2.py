import random
def flips():
  deck=[1]*4 +[0]*48
  random.shuffle(deck)
  cards_turned=0
  for card in deck:
    cards_turned+=1
    if card==1:
       return cards_turned
trials=100000
cards_flipped=sum(flips() for _ in range(trials))
expected_val=cards_flipped/trials
print(expected_val)


    
  
      
      
