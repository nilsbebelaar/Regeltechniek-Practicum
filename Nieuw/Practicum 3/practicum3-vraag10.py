"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pyplot as plt
import control
from animation_simulation import simulate_and_animate_results

# Definieer de waarde van Kp en Kd
Kp = 100
Kd = 5
m = 1  # kg

# Definieer de overdrachtsfunctie H(s)
teller = [Kd, Kp]
noemer = [m, Kd, Kp]
H = control.tf(teller, noemer)
print(H)
#print(control.poles(H))

for Kd in range(1,100):
    num = np.array([Kd * m, Kp * m])
    den = np.array([Kd * m, Kp * m + 1])
    H = control.tf(num, den)
    info = control.step_info(H)

# Simuleer het gesloten lussysteem voor een stappingang
#anim = simulate_and_animate_results(Kp, Kd)

#plt.show()
