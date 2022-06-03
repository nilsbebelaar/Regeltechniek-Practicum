"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pylab as plt
import control
M = 1.0
teller = np.array([M,0.0,0.0])
noemer = np.array([1.0])
H = control.tf(teller, noemer)

K = 100
Sys1 = K*H
Sys2 = 1



Hclosed = control.feedback(Sys1,Sys2) 

print(Hclosed)

print("Pole: ",Hclosed.pole())
print("Zero: ",Hclosed.zero())

t_closed, y_closed = control.step_response(Hclosed) 


tijd_totaal = 0
j = 0


for i in range(len(y_closed)):
    if(y_closed[i] > 0.999):
        tijd_totaal += t_closed[i]
       
    j += 1

T = 1/(tijd_totaal/j)*2*3.14
print(f'Trillings tijd: {T}')

plt.plot(t_closed, y_closed)
plt.ylabel('Stap reponsie')
plt.xlabel('Tijd [s]')

plt.show()