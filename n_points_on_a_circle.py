import numpy as np
import random
import matplotlib.pyplot as plt
def n_points(n,angle,trials=100000):
  prob_inside=angle/360.0
  fav_pts=0 #prob of being in the given angle
  for _ in range(trials):
    if_in_angle=np.random.rand(n-1)
    if np.all(if_in_angle<=prob_inside):
      fav_pts+=1
  return (fav_pts/trials)*n

angles=[30,60,90,120,150,180]
simulated_prob=[n_points(4,a)*100 for a in angles]
actual_prob=[4*(a/360)**(3)*100 for a in angles]
plt.figure(figsize=(7,4))
plt.plot(angles,actual_prob,label="Actual prob",color="red")
plt.plot(angles,simulated_prob,label="Simulated Prob",color="blue")
plt.xlabel("Angle in deg")
plt.ylabel("prob")
plt.show()

    
  
  
  
    
    
