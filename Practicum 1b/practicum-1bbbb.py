"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
from turtle import color
import numpy as np
import matplotlib.pylab as plt
import control
import control.matlab as cm


T = np.array([5.0])
N = np.array([1.0, 5.0])
H = control.tf(T, N)

print(H)

t = np.arange(0, 10, 0.01)  # definitie tijdsvector
u = np.sin(5*t)  # zelf definiëren
y, t_dummy, x_dummy = cm.lsim(H, u, t)  # u input, t time, of
y = cm.lsim(H, u, t)[0]  # u input, t time # alternatieve notatie

plt.plot(t,u)
plt.plot(t,y)
plt.show()
