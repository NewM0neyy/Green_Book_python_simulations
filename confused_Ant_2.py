import random
def random_walk(trials=100000):
 total_steps=0
 for _ in range(trials):
    state=0
    steps=0
    while True:
      steps+=1
      if state==0:
        state=1
      elif state==1:
        state=random.choice([0,2,2])
      elif state==2:
        state=random.choice([1,1,3])
      elif state==3:
        state=2
      if state==0:
        break
    total_steps+=steps
 return total_steps/trials
print(random_walk())



      
    
    
