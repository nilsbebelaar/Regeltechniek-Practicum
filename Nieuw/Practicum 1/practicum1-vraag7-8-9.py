"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import math as mth
import numpy as np
import matplotlib.pylab as plt
import control

teller = np.array([18.0])
noemer = np.array([1.0, 1.2, 36])
H = control.tf(teller, noemer)

print("Pole: ", H.pole())
print("Zero: ", H.zero())

K = 100
Sys1 = K*H
Sys2 = 1
Hclosed = control.feedback(Sys1, Sys2)

print(Sys1)
print(Hclosed)

t_open, y_open = control.step_response(Sys1, T=np.linspace(0, 30, 10000))
t_closed, y_closed = control.step_response(Hclosed, T=np.linspace(0, 12, 5000))

info_openlus = control.step_info(Sys1)
info_closed = control.step_info(Hclosed)

print("\n\n===== control.step_info(open-loop): =====")
for k in info_openlus:
    print(f"{k}:  {info_openlus[k]}")

print("\n\n===== control.step_info(closed-loop): =====")
for k in info_closed:
    print(f"{k}:  {info_closed[k]}")

plt.plot(t_open, y_open, t_closed, y_closed)
plt.ylabel('Stap reponsie')
plt.xlabel('Tijd [s]')
plt.legend(["Open", "Gesloten"])


plt.show()
