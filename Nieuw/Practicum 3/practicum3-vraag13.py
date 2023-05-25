"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pyplot as plt
import control
from animation_simulation import simulate_and_animate_results

# Definieer de waarde van Kp en Kd
Kp = 100
Kd = 24.86
m = 1  # kg
teller = [Kd, Kp]
noemer = [m, Kd, Kp]
H_pd = control.tf(teller, noemer)

t = np.linspace(0, 3, 1000)  # definitie tijdsvector
u5 = np.sin(5*t)  # zelf definiëren
y5 = control.forced_response(H_pd, t, u5)[1]
u10 = np.sin(10*t)  # zelf definiëren
y10 = control.forced_response(H_pd, t, u10)[1]

u3 = u5/2 + u10/2
y3 = control.forced_response(H_pd, t, u3)[1]


# maakt plot 2 aan

plt.plot(t, u5, label=r"$\sin(5t)$", linestyle='dashed', color='blue')
plt.plot(t, u10, label=r"$\sin(10t)$", linestyle='dashed', color='red')
plt.plot(t, u3, label=r"$\frac{1}{2}\sin(5t) + \frac{1}{2}\sin(10t)$", linestyle='dashed', color='green')

plt.plot(t, y5, label=r"response to $\sin(5t)$", color='blue')
plt.plot(t, y10, label=r"response to $\sin(10t)$", color='red')
plt.plot(t, y3, label=r"response to $\frac{1}{2}\sin(5t) + \frac{1}{2}\sin(10t)$", color='green')
plt.xlabel('Tijd [s]')
plt.legend()
plt.show()
