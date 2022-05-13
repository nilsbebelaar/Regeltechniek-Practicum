"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
from tkinter import Y
import numpy as np
import matplotlib.pylab as plt 
import control


def find_doorschot(yrange, eind_waarde):
    doorschot = max(yrange) - eind_waarde
    index = yrange.tolist().index(max(yrange))
    return doorschot, index*((11.5)/len(yrange))


teller = np.array([18.0]) 
noemer = np.array([1.0, 1.2,36]) 
H = control.tf(teller,noemer)
print(H)

print("Pole: ",H.pole())
print("Zero: ",H.zero())




K = 100
Sys1 = K*H
Sys2 = 1
Hclosed = control.feedback(Sys1,Sys2) 

t_open, y_open = control.step_response(Sys1)  
t_closed, y_closed = control.step_response(Hclosed) 

print(y_open)



print(find_doorschot(y_open,50))
print(find_doorschot(y_closed,1))

plt.plot(t_open,y_open, t_closed, y_closed)
plt.ylabel('Stap reponsie')
plt.xlabel('Tijd [s]')
plt.legend(["Open","Gesloten"])


plt.show()