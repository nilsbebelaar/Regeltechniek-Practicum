"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import numpy as np
import matplotlib.pylab as plt
import control
import control.matlab as cm

T = np.array([5.0])
N = np.array([1.0, 5.0])
H = control.tf(T,N)

print(H)
for w in [0, 1, 5, 10, 100]:
    Hw = control.evalfr(H, 1j * w)
    print("W:",w,"H(jw):",Hw)
    print("W:",w,"|H(jw)|:",np.abs(Hw))
    print("W:",w,"args(H(jw)):",np.degrees(np.angle(Hw)))