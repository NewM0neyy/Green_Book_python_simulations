import random
def random_walk(trials=100000,p=1/3,max_steps=1000):
  reaching_one=0
  for _ in range(trials):
    current_step=0
    step=0
    while step<max_steps:
      
      r=random.random()
      if r<p:
        current_step+=1
      else:
        current_step-=1
      if current_step==1:
        reaching_one+=1
        break
      step+=1
  return reaching_one/trials
print(random_walk())
  
      
      
      
