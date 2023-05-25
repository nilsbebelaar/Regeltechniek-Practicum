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


G = control.tf([1], [m, 0, 0])
Lp = Kp * G
Lpd = (Kp + Kd * G.s) * G

mag, phase, omega = control.bode(Lp, omega=np.logspace(-2, 3, 300), dB=True, label="$L_{p}(s)$")
mag, phase, omega = control.bode(Lpd, omega=np.logspace(-2, 3, 300), dB=True, label="$L_{pd}(s)$")

all_axes = plt.gcf().get_axes()
plt.sca(all_axes[0])
plt.title("Bode plot van $L_{p}(s)$ en $L_{pd}(s)$")
plt.legend()
plt.show()
