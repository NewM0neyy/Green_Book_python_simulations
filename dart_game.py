
import numpy as np
def throws(trials=100000):
    d1=np.random.uniform(0,1,size=trials)
    d2=np.random.uniform(0,1,size=trials)
    d3=np.random.uniform(0,1,size=trials)
    given_cond=d2>d1
    fav_cond=given_cond & (d3>d1)
    p=np.sum(fav_cond)/np.sum(given_cond)
    return p
print(throws())


    
    .
