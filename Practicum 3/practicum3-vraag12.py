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

teller = [Kp]
noemer = [m, 0, Kp]
H_p = control.tf(teller, noemer)
print(H_p)

mag, phase, omega = control.bode(H_pd, omega=np.logspace(-0.5, 2.5, 300), dB=True, label="$T_{pd}(s)$")


all_axes = plt.gcf().get_axes()
plt.sca(all_axes[0])
plt.title("Bode plot van $T_{pd}(s)$ gesloten lus")
plt.legend()
plt.show()
