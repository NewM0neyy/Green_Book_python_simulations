import numpy as np
def game(trials=100000):
  car=np.random.randint(0,3,size=trials)
  choice=np.random.randint(0,3,size=trials)
  stay=np.mean(car==choice)
  switch=np.mean(car!=choice)
  prob=[stay,switch]
  x=["stay","switch"]
  plt.figure(figsize=(10,6))
  plt.bar(x,prob)
  plt.show()
game()
               


