"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import numpy as np
import matplotlib.pylab as plt
import control
import control.matlab

omega_n = 100  # rad/s
t = np.logspace(1.5, 2.5, 10000)    #tijd voor de bode plot
_t = np.arange(0, 0.5, 0.01)        #tijd voor de forced response
u = np.sin(5*_t)                    #sinus golf voor de forced response


zetas = [0.01, 0.1, 0.2, 0.5, 1, 2]
x_punt = [100, 100, 100, 100, 100, 100]
y_punt = []

#forced response spullen
labes = []
point_list = []

for zeta in zetas:
    ##regelaar dingen
    T = np.array([omega_n ** 2])                                #T = teller van de breuk niet de tijd
    N = np.array([1.0, 2 * zeta * omega_n, omega_n ** 2])       #N = noemer van de breuk
    H = control.tf(T, N)
    ##regelaar dingen einde
    print(f'Zeta: {zeta}')
    print(H)

    y_punt.append(20 * np.log10(1 / (2 * zeta)))

    #forced response
    y = control.forced_response(H,_t,u)[1] 
    point_list.append(y)
    labes.append(f'Zeta {zeta}')

    #bode plot
    mag, phase, omega = control.bode(H, omega=t, label=f"$\zeta$={zeta}")

#bode plot
all_axes = plt.gcf().get_axes()
plt.sca(all_axes[0])
plt.scatter(x_punt, y_punt, label=r'$\frac{1}{2\zeta}$')
plt.legend()

#maakt plot 2 aan
fig, ax = plt.subplots(1)
#voeg punten toe
for points in point_list:
    ax.plot(_t,points)
ax.plot(_t,u)
#label de punten
labes.append("sin")
plt.legend(labes)


plt.show()
