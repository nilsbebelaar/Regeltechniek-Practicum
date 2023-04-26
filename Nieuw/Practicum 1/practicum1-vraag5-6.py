import numpy as np 
import matplotlib.pylab as plt 
import control as ctrl

teller = np.array([2.0]) # teller: 2.0 * s^0
noemer = np.array([1.0, -3.0]) # noemer: 1.0 * s^1 – 3.0 * s^0
H = ctrl.tf(teller,noemer)

print("Pole: ", H.pole())
print("Zero: ", H.zero())

time = [2.2, 3.0, 6.0, 6.0]

for i, K in enumerate([0.1, 1, 1.5, 10]):

    print(K)
    Sys1 = K*H
    Sys2 = 1
    Hclosed = ctrl.feedback(Sys1, Sys2)

    y, t = ctrl.step_response(Hclosed, T=time[i])

    plt.plot(t, y)

plt.ylabel('Stapresponsie')
plt.xlabel('Tijd [s]')
plt.legend(["0.1", "1", "1.5", "10"])
plt.show()
