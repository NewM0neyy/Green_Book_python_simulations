import random
import numpy as np
def numb_of_girls(trials=100000,n=5):
  number_of_girls=0
  number_of_boys=0
  gender=['Boy','Girl']
  for _ in range(trials):
    child=random.choice(gender)
    if child=='Girl':
      number_of_girls+=1
    else:
      while child!='Girl':
        child=random.choice(gender)
        number_of_boys+=1
      number_of_girls+=1
  total_population=number_of_girls+number_of_boys
  p_girl=number_of_girls/total_population
  p_boy=number_of_boys/total_population
  print(f"Propulation percentage of Girls: {p_girl}")
  print(f"Population Percentage of boys: {p_boy}")
        
numb_of_girls()       
      
    
