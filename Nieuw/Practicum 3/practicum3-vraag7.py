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

mag, phase, omega = control.bode(H, omega=np.logspace(-2, 3, 300), dB=True)

# plt.legend()
plt.show()

# Bepaal de fase L(jω) voor een specifieke frequentie ω
target_omega = 10  # Pas aan naar de gewenste frequentie
index = np.abs(omega - target_omega).argmin()  # Vind het indexnummer het dichtst bij de doelfrequentie
phase_at_target_omega = phase[index]  # Haal de fase op bij de doelfrequentie

print("Fase L(jω) op ω =", target_omega, "is", phase_at_target_omega, "graden")