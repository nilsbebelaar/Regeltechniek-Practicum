"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import numpy as np
import matplotlib.pylab as plt 
import control

teller = np.array([2.0]) 
noemer = np.array([1.0, -3.0]) 
H = control.tf(teller,noemer)
print(H)

print("Pole: ",H.pole())
print("Zero: ",H.zero())



for i in [0.1, 1, 1.5, 10]:

    K = i
    print(i)
    Sys1 = K*H
    Sys2 = 1
    Hclosed = control.feedback(Sys1,Sys2) 

    y,t = control.step_response(H)  

    plt.plot(t,y)
    plt.ylabel('Stap reponsie')
    plt.xlabel('Tijd [s]')
    plt.legend(["a","b","c","d"])



plt.show()