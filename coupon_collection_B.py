import numpy as np
import matplotlib.pyplot as plt
def collecting(trials=100000,no_of_boxes=5,unique_toys=5):
  number_of_unique_toys=0
  
  for _ in range(trials):
    collected_toys=set()
    for _ in range(no_of_boxes):
      toy=np.random.randint(1,unique_toys)
      collected_toys.add(toy)
    number_of_unique_toys+=len(collected_toys)
  return number_of_unique_toys/trials

number_of_boxes=np.arange(1,6)
number_of_unique_toys=np.arange(2,6)
expected_boxes_1=[collecting(no_of_boxes=i,unique_toys=3) for i in number_of_boxes]  
expected_boxes_2=[collecting(no_of_boxes=5,unique_toys=i) for i in number_of_unique_toys]
fig, (ax1,ax2) =plt.subplots(1,2,figsize=(10,5))  
ax1.plot(number_of_boxes,expected_boxes_1,color='green')
ax2.plot(number_of_unique_toys,expected_boxes_2,color='red')
ax1.set_xlabel("Number of boxes w/ fixed number of unique toys")
ax1.set_ylabel("Expected number of unique toys collected")
ax2.set_xlabel("Number of unique toys to be collected")
ax2.set_ylabel("Expected NUmber of unique toys collected")
plt.tight_layout()
plt.show() 

    
  
  
