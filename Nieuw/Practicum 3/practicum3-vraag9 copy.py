"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pyplot as plt
import control


# Definieer de waarde van Kp en Kd
Kp = 100
Kd = 100
m = 1  # kg

teller = np.array([Kd*m,Kp*m,0,0])
noemer = np.array([Kd*m,Kp*m,0,1])
H = control.tf(teller, noemer)




