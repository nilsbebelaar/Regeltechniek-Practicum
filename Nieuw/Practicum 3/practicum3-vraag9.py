"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pyplot as plt
import control


# Definieer de waarde van Kp en Kd
Kp = 100
Kd = 5
m = 1  # kg

# Definieer de overdrachtsfunctie H(s)
teller = [Kd, Kp]
noemer = [m, Kd, Kp]
H = control.tf(teller, noemer)
print(H)
print(control.poles(H))

# Simuleer het gesloten lussysteem voor een stappingang
t, y = control.step_response(H)

# Plot de simulatieresultaten
plt.plot(t, y)
plt.xlabel('Tijd')
plt.ylabel('Uitgang')
plt.title('Staprespons van het gesloten lussysteem')
plt.grid(True)
plt.show()
