import random
def both_boys(trials=100000):
  both_boys=0
  gender=['Boy','Girl']
  child1='Boy'
  for _ in range(trials):
    child2=random.choice(gender)
    if child2=='Boy'and child1=='Boy':
      both_boys+=1
  print(both_boys/trials)
both_boys()
