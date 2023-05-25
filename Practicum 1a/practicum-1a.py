"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import numpy as np
import matplotlib.pylab as plt
import control

teller = np.array([2.0])
noemer = np.array([1.0, -3.0])
H = control.tf(teller, noemer)
print(H)
print("Pole: ", H.pole())
print("Zero: ", H.zero())

time = [2.2, 3.0, 6.0, 6.0]

for i, K in enumerate([0.1, 1, 1.5, 10]):

    print(K)
    Sys1 = K*H
    Sys2 = 1
    Hclosed = control.feedback(Sys1, Sys2)

    y, t = control.step_response(Hclosed, T=time[i])

    plt.plot(t, y)


plt.ylabel('Stap reponsie')
plt.xlabel('Tijd [s]')
plt.legend(["0.1", "1", "1.5", "10"])
plt.show()