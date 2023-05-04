"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pylab as plt
import control

t = np.arange(0, 10, 0.01)  # definitie tijdsvector
u = np.sin(5*t)  # zelf definiëren

plt.plot(t,u)

plt.show()