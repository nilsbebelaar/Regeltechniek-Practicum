"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pylab as plt
import control

M = 1.0
teller = np.array([1])
noemer = np.array([M, 5.0, 0.0])
H = control.tf(teller, noemer)

print(H)

mag, phase, omega = control.bode(H, omega=np.logspace(-1, 2, 300), dB=True, label="$L(s)$")

all_axes = plt.gcf().get_axes()
plt.sca(all_axes[0])
plt.title("Bode plot van $L(s)$ open lus")
plt.legend()
plt.show()
