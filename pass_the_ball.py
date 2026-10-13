import random
def passin(trials=100000):
  num_people=5
  end_game=0 #when you end the game 
  for _ in range(trials):
    current_holder=0
    while True:
      action=random.choice(['L','R','K'])
      if action=='K':
        if current_holder==0:
          end_game+=1
        break
      elif action=='L':
        current_holder=(current_holder-1)%num_people
      elif action=='R':
        current_holder=(current_holder+1)%num_people
  p=end_game/trials
  return p
print(passin())
