"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import numpy as np
import matplotlib.pylab as plt
import control

T = np.array([5.0])
N = np.array([1.0, 5.0])
H = control.tf(T, N)

print(H)

#control.bode(H, omega=np.logspace(-1,5,300))  # alleen een plot
mag, phase, omega = control.bode(H, omega=np.logspace(-2,3,300),dB=True)  # een plot en nummerieke uitvoer

x = [0, 1, 5, 10, 100]
y1 = []
y2 = []

for w in [0, 1, 5, 10, 100]:
    Hw = control.evalfr(H, 1j * w)
    y1.append(20 * np.log10(np.abs(Hw)))
    y2.append(np.degrees(np.angle(Hw)))

all_axes = plt.gcf().get_axes()
plt.sca(all_axes[0])
plt.scatter(x, y1)

plt.sca(all_axes[1])
plt.scatter(x, y2)

plt.show()
