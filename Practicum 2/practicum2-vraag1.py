"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import numpy as np
import matplotlib.pylab as plt
import control


T = np.array([5.0])
N = np.array([1.0, 5.0])
H = control.tf(T,N)

print(H)