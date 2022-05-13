"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import math as mth
import numpy as np
import matplotlib.pylab as plt 
import control


def find_doorschot(yrange, eind_waarde):
    doorschot = max(yrange) - eind_waarde
    index = yrange.tolist().index(max(yrange))
    return doorschot, index*((11.5)/len(yrange))

def static_error(y_range,eind_waarde):
    StatError = 0
    for i in range(5): 
        StatError = StatError +  eind_waarde-y_range[-i]
    return StatError/5

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


d1, t1 = find_doorschot(y_open,50)
d2, t2 = find_doorschot(y_closed,1)
print("Doorschot Open","Waarde:",round(d1,2), "Tijdstip", round(t1,2))
print("Static Error Open",static_error(y_open,50))

print("Doorschot Open","Waarde:", round(d2,2), "Tijdstip", round(t2,2))
print("Static Error Open",static_error(y_closed,1))


plt.plot(t_open,y_open, t_closed, y_closed)
plt.ylabel('Stap reponsie')
plt.xlabel('Tijd [s]')
plt.legend(["Open","Gesloten"])


plt.show()