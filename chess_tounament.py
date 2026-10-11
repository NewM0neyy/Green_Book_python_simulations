def tournament(n=4,trials=100000):
  numb_of_players=2**n
  meet_in_last_round=0
  for _ in range(trials):
    players=list(range(1,numb_of_players+1))
    met=False
    while len(players) >2:
      np.random.shuffle(players)
      next_round=[]
      for i in range(0,len(players),2):
        p1,p2=players[i],players[i+1]
        if {p1,p2}=={1,2}:
          met=True
          break
        next_round.append(min(p1,p2))
      if met:
        break
      players=next_round
      if not met and set(players)=={1,2}:
        meet_in_last_round+=1
    
  return meet_in_last_round/trials

def main():
  n=[2,3,4,5,6]
  probs=[]
  for i in n:
    probs.append(tournament(i))
  plt.plot(n,probs,marker="o",color="red")
  plt.xlabel("Number of Players")
  plt.ylabel("Prob of 1 and 2 meetin in final round")
  plt.show()

if __name__=="__main__":
  main()
