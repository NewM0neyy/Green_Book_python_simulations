import random
def b_n_g(trials=100000):
  valid_mother=0
  both_boys=0
  gender=['Boy','Girl']
  for _ in range(trials):
    child1=random.choice(gender)
    child2=random.choice(gender)
    if child1=='Boy' or child2=='Boy':
      valid_mother+=1
      if child1=='Boy' and child2=='Boy':
        both_boys+=1
  print( both_boys/valid_mother)
b_n_g()
    
