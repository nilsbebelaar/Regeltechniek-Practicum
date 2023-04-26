"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pylab as plt
import control
M = 1.0
teller = np.array([M])
noemer = np.array([1.0,0.0,0.0])
H = control.tf(teller, noemer)

K = 100
Sys1 = K*H
Sys2 = 1

Hclosed = H #control.feedback(Sys1,Sys2) 

print(Hclosed)

print("Pole: ",Hclosed.pole())
print("Zero: ",Hclosed.zero())

#t_closed, y_closed = control.step_response(Hclosed) 
mag, phase, omega = control.bode(Hclosed, omega=np.logspace(-1,1,300))
print(phase)


plt.show()