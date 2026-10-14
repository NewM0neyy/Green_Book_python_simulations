import random
def candy(trials=100000):
  jar=['R']*10+['B']*20+['G']*30
  fav=0
  for _ in range(trials):
    random.shuffle(jar)
    last_r=len(jar)-1-jar[::-1].index('R')
    last_b=len(jar)-1-jar[::-1].index('B')
    last_g=len(jar)-1-jar[::-1].index('G')
    if last_r<last_b and last_r<last_g:
      fav+=1
  p=fav/trials
  return p
print(candy())
