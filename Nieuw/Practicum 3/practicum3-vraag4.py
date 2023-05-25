"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pylab as plt
import control
from math import pi
from animation_simulation import simulate_and_animate_results

Kp = 100
m = 1.0  # kg

teller = np.array([m])
noemer = np.array([1, 0, 0])
H = control.tf(teller, noemer)

Sys1 = H * Kp
Sys2 = 1

H_closed = control.feedback(Sys1, Sys2)

print(H_closed)

print("Pole: ", H_closed.pole())
print("Zero: ", H_closed.zero())

T = np.linspace(0, 2.5, 1000)

t_closed, y_closed = control.step_response(H_closed, T=T)
info_closed = control.step_info(H_closed, T=T)

tijd_totaal = 0
j = 0

for i in range(len(y_closed)):
    if (y_closed[i] > 0.999):
        tijd_totaal += t_closed[i]

    j += 1

T = 1/(tijd_totaal/j)*2*pi
print(f'Trillingstijd: {T}')
print(f'Frequentie: {1/T}')

print("\n\n===== control.step_info(closed-loop): =====")
for k in info_closed:
    print(f"{k}:  {info_closed[k]}")

plt.plot(t_closed, y_closed)
plt.ylabel('Stap reponsie')
plt.xlabel('Tijd [s]')
plt.show()

anim = simulate_and_animate_results(Kp, 0)
plt.show()
