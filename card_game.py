import numpy as np
import matplotlib.pyplot as plt
def card_game(trials=100000):
  deck=np.repeat(np.arange(1,14),4)
  shuffle=np.array([np.random.permutation(deck) for _ in range(trials)])
  my_card=shuffle[:,0]
  opp_card=shuffle[:,1]
  win_win=np.sum(my_card>opp_card)
  opp_win=np.sum(my_card<=opp_card)
  win_prob=(win_win/trials)
  lose_prob=1.0-win_prob
  x_labels=["You win","opp wins"]
  y_values=[win_prob,lose_prob]
  print(f"Winning prob {win_prob}")
  plt.bar(x_labels,y_values)
  plt.show()
def main():
    card_game()
main()
  
