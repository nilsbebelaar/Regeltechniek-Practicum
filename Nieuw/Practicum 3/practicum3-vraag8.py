"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pyplot as plt
import control

# Definieer de overdrachtsfunctie G(s)
num = [1]
den = [1, 2, 1]
H = control.tf(num, den)

# Definieer de waarde van Kp
Kp = 100

# Definieer de lusversterking L(s) = Kp * G(s)
L = Kp * H

# Definieer de overdrachtsfunctie van het gesloten lussysteem
T = L / (1 + L)

mag, phase, omega = control.bode(T, omega=np.logspace(-0.5, 2.5, 300), dB=True)

t = np.linspace(0, 3, 1000)  # definitie tijdsvector
u5 = np.sin(5*t)  # zelf definiëren
y5 = control.forced_response(T,t,u5)[1] 
u10 = np.sin(10*t)  # zelf definiëren
y10 = control.forced_response(T,t,u10)[1] 


#bode plot
all_axes = plt.gcf().get_axes()
plt.sca(all_axes[0])
plt.legend()

#maakt plot 2 aan
fig, ax = plt.subplots(1)
ax.plot(t,u5, label=f"$\sin(5t)$")
ax.plot(t,u10, label=f"$\sin(10t)$")
plt.plot(t,y5, label=f"response to $\sin(5t)$")
plt.plot(t,y10, label=f"response to $\sin(10t)$")
plt.xlabel('Tijd [s]')
plt.legend()
plt.show()