import numpy as np
import matplotlib.pyplot as plt
def collection(trials=10000,n=5):
  boxes=0
  for _ in range(trials):
    coupon_collected=set()
    boxes_opened=0
    count=0
    while len(coupon_collected)<n :
      coupon=np.random.randint(0,n)
      coupon_collected.add(coupon)
      boxes_opened+=1
      count+=1
    boxes+=boxes_opened
  return boxes/trials
n=np.arange(1,6)
expected_boxes=[collection(n=i) for i in n]
plt.figure(figsize=(10,6))
plt.plot(n,expected_boxes,color='green')
plt.xlabel("No of unique toys")
plt.ylabel("Number of boxes needed to be opened")
plt.show()

