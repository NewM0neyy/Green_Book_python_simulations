import mpmath

mpmath.mp.dps=500 # dynamic precision usin mpmath 
val=(mpmath.mpf(1)+mpmath.mpf(2)**0.5)**1000
integer_dig=str(int(val))
print(f"The hundreth dig from the left:{integer_dig[99]}")
