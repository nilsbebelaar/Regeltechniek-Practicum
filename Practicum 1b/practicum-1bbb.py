"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import numpy as np
import matplotlib.pylab as plt
import control
import control.matlab as cm

T = np.array([5.0])
N = np.array([1.0, 5.0])
H = control.tf(T, N)

print(H)

control.bode(H)  # alleen een plot
mag, phase, omega = control.bode(H)  # een plot en nummerieke uitvoer

x = [0, 1, 5, 10, 100]
y = []

for w in [0, 1, 5, 10, 100]:
    Hw = control.evalfr(H, 1j * w)
    print(20 * np.log10(np.abs(Hw)))
    y.append(np.abs(Hw))

# control.singular_values_plot(H)
# plt.scatter(x, y)

plt.show()
