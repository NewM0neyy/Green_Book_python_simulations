import numpy as np
def population(trials=100000, max_steps=40,max_population=150):
  die=0
  outcomes=np.arange(0,4)
  for _ in range(trials):
    current=1
    for _ in range(max_steps):
      if current==0:
        die+=1
        break
      if current>=max_population:
        break
      outcome=np.random.choice(outcomes,size=current)
      current=np.sum(outcome)
    else:
       if current==0:
         die+=1
  return die/trials

print(population())
    
    

      
