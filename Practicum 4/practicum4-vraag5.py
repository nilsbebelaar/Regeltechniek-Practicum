"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pylab as plt
import control

Kp = 100
Kd = 17
M = 1.0

H = control.tf([1],
               [M, 5.0, 0.0])

H_rondgaand = control.tf([Kd, Kp],
                         [M, 5, 0])

H_feedback = control.tf([Kd, Kp],
                        [M, 5+Kd, Kp])

# Hclosed = control.feedback(H, 1)

print("\n===== H_rondgaand: =====")
print(H_rondgaand)
print("\n===== H_feedback: =====")
print(H_feedback)

mag, phase, omega = control.bode(H_rondgaand, omega=np.logspace(-1, 2, 300), dB=True, label="$L(s)$")

all_axes = plt.gcf().get_axes()
plt.sca(all_axes[0])
plt.title("Bode plot van $L(s)$ open lus")
plt.legend()
plt.show()
