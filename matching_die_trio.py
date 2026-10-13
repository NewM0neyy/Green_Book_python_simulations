import numpy as np

def rollin_die(trials=100000):
  first_roll=np.sort(np.random.randint(1,7,size=(trials,3)),axis=1)
  second_roll=np.sort(np.random.randint(1,7,size=(trials,3)),axis=1)
  same_roll=np.all(first_roll==second_roll,axis=1)
  tri=np.arange(1,trials+1)
  prob=np.cumsum(same_roll)/tri
  plt.figure(figsize=(10,6))
  plt.plot(tri,prob)
  plt.xlabel("Number of trials")
  plt.ylabel("prob")
  plt.show()

rollin_die()
