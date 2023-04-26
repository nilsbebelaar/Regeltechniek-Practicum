import numpy as np 
import matplotlib.pylab as plt 
import control as ctrl

teller = np.array([2.0]) # teller: 2.0 * s^0
noemer = np.array([1.0, -3.0]) # noemer: 1.0 * s^1 – 3.0 * s^0
H = ctrl.tf(teller,noemer)
print(H)

print(H.pole())
print(H.zero())