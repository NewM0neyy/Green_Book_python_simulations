import numpy as np
import matplotlib.pyplot as plt
def drunk_pass(target,seat=100,trials=100000):
  correct_seat=0
  for _ in range(trials):
    seats_taken=set()
    drunk=np.random.randint(1,seat+1)
    seats_taken.add(drunk)
    for i in range(2,target):
      if i in seats_taken:
        remainin_seats=[s for s in range(1,seat+1) if s not in seats_taken]
        seats_taken.add(np.random.choice(remainin_seats))
      else:
        seats_taken.add(i)
    if target not in seats_taken:
      correct_seat+=1
  return correct_seat/trials

passenger_numbers=range(1,101)
prob=[drunk_pass(t,seat=100,trials=1000) for t in passenger_numbers]
plt.plot(passenger_numbers,prob)
plt.xlabel("Passanger Number")
plt.ylabel("Success Prob")
plt.show()

           
    
  
  
