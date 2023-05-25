"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pyplot as plt
import control

# Definieer de waarde van Kp en Kd
Kp = 100
Kd = 24.86
m = 1  # kg

G = control.tf([1], [m, 0, 0])
C = Kp

L = G * C

mag, phase, omega = control.bode(L, omega=np.logspace(-2, 3, 300), dB=True, label="$T(s)$")

all_axes = plt.gcf().get_axes()
plt.sca(all_axes[0])
plt.title("Bode plot van $L(s)$")
plt.legend()
plt.show()

# Bepaal de fase L(jω) voor een specifieke frequentie ω
target_omega = 10  # Pas aan naar de gewenste frequentie
index = np.abs(omega - target_omega).argmin()  # Vind het indexnummer het dichtst bij de doelfrequentie
phase_at_target_omega = phase[index]  # Haal de fase op bij de doelfrequentie

print("Fase L(jω) op ω =", target_omega, "is", phase_at_target_omega, "graden")
