"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import numpy as np
import matplotlib.pylab as plt
import control
import control.matlab

omega_n = 100  # rad/s

zetas = [0.01, 0.1, 0.2, 0.5, 1, 2]
x_punt = [100, 100, 100, 100, 100, 100]
y_punt = []

for zeta in zetas:
    T = np.array([omega_n ** 2])
    N = np.array([1.0, 2 * zeta * omega_n, omega_n ** 2])
    H = control.tf(T, N)
    print(H)

    y_punt.append(20 * np.log10(1 / (2 * zeta)))
    mag, phase, omega = control.bode(H, omega=np.logspace(
        1.5, 2.5, 10000), label=f"$\zeta$={zeta}")

all_axes = plt.gcf().get_axes()
plt.sca(all_axes[0])
plt.scatter(x_punt, y_punt, label=r'$\frac{1}{2\zeta}$')
plt.legend()
plt.show()
