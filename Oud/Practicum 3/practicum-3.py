"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pylab as plt
import control

Kp = 100
Kd = 17



M = 1.0
teller = np.array([Kd,Kp])
noemer = np.array([M,5.0,0.0])
H = control.tf(teller, noemer)


Sys1 = H
Sys2 = 1

Hclosed = control.feedback(Sys1,Sys2) 

print(Hclosed)

print("Pole: ",Hclosed.pole())
print("Zero: ",Hclosed.zero())
t = np.linspace(0,10,200)
t_closed, y_closed = control.step_response(Hclosed,t) 
#mag, phase, omega = control.bode(Hclosed)



plt.plot(t_closed, y_closed)
plt.scatter([0.5],[1.0])
plt.ylabel('Stap reponsie')
plt.xlabel('Tijd [s]')
plt.show()