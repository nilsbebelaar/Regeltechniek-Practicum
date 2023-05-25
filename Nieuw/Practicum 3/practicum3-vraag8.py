"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pyplot as plt
import control

# Definieer de waarde van Kp en Kd
Kp = 100
Kd = 24.86
m = 1  # kg


G = control.tf([1], [m, 0, 0])
C = Kp

L = G * C

T = L / (1 + L)
print(control.poles(T))

mag, phase, omega = control.bode(T, omega=np.logspace(0, 2, 4000), dB=True, label="$T(s)$")

t = np.linspace(0, 3, 1000)  # definitie tijdsvector
u5 = np.sin(5*t)  # zelf definiëren
y5 = control.forced_response(T, t, u5)[1]
u10 = np.sin(10*t)  # zelf definiëren
y10 = control.forced_response(T, t, u10)[1]


# bode plot
all_axes = plt.gcf().get_axes()
plt.sca(all_axes[0])
plt.title("Bode plot van $T(s)$")
plt.legend()

# maakt plot 2 aan
fig, ax = plt.subplots(1)
ax.plot(t, u5, label=f"$\sin(5t)$")
ax.plot(t, u10, label=f"$\sin(10t)$")
plt.plot(t, y5, label=f"response to $\sin(5t)$")
plt.plot(t, y10, label=f"response to $\sin(10t)$")
plt.xlabel('Tijd [s]')
plt.legend()
plt.show()
