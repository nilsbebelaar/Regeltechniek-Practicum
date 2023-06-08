"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pylab as plt
import control

Kd = 10
Kp = 5*Kd
M = 1.0

T = control.tf([Kd, Kp],
                        [M, 5+Kd, Kp])

print("\n===== T(s): =====")
print(T)


t, y = control.step_response(T, T=np.linspace(0, 2, num=1000))

# Plot de simulatieresultaten
plt.plot(t, y, label="$T(s)$")
plt.xlabel('Tijd $(s)$')
plt.ylabel('Uitgang')
plt.title('Staprespons van het gesloten lussysteem $T(s)$')
plt.grid(True)
plt.legend()
plt.show()
