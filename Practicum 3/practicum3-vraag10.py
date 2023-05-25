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

overshoot = 100
Kd = 24.5
while overshoot > 10:
    Kd += 0.001
    teller = [Kd, Kp]
    noemer = [m, Kd, Kp]
    H = control.tf(teller, noemer)
    overshoot = control.step_info(H)['Overshoot']

print(H)
print(f"Kd: {Kd}, Kp: {Kp}")
print(control.step_info(H))
t, y = control.step_response(H)

# Plot de simulatieresultaten
plt.plot(t, y)
plt.xlabel('Tijd')
plt.ylabel('Uitgang')
plt.title('Staprespons van het gesloten lussysteem')
plt.grid(True)
plt.show()

anim = simulate_and_animate_results(Kp, Kd, simulation_time=1)
plt.show()
