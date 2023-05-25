"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import numpy as np 
import matplotlib.pylab as plt 
import control as ctrl

teller = np.array([2.0]) # teller: 2.0 * s^0
noemer = np.array([1.0, -3.0]) # noemer: 1.0 * s^1 – 3.0 * s^0
H = ctrl.tf(teller,noemer)
print(H)

t = np.linspace(0,10,200)
y = ctrl.step_response(H,t)[0] # selecteer 0e element voor alleen output
plt.plot(t,y)
plt.ylabel('Stapresponsie')
plt.xlabel('Tijd [s]')
plt.legend('Open lus')
plt.show()
