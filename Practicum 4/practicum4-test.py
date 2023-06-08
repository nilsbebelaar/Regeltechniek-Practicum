"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""

import numpy as np
import matplotlib.pylab as plt
import control

def CaclulateInfo(mag, phase, omega):

    wc, pm, ts, = 0,0,0
 
    wcFreqIndex = -1
    ## calculate wc
    prev = None
    for i in range(0,len(omega)):
        if(mag[i] < 1):
            if(prev == None):
                print(mag[i],omega[i])
                wc = omega[i]
                prev = mag[i]
                wcFreqIndex = i
            elif(prev < mag[i]):
                print(mag[i],omega[i])
                wc = omega[i]
                prev = wc
                wcFreqIndex = i
    
    if(wcFreqIndex == -1):
        return -1,-1,-1
    
    pm = 180 + phase[wcFreqIndex]*57.2957795
    ts = 460/(pm*wc)

    return wc, pm, ts

Kp = 50

Kd = 10
M = 1.0

G = control.tf([1],
               [M, 5.0, 0.0])
C = Kp + Kd*G.s

L = C*G if (C != 0) else G



# Hclosed = control.feedback(H, 1)

mag, phase, omega = control.bode(C, omega=np.logspace(-1, 2, 300), dB=True, label="$C(s)$")

mag, phase, omega = control.bode(G, omega=np.logspace(-1, 2, 300), dB=True, label="$G(s)$")

mag, phase, omega = control.bode(L, omega=np.logspace(-1, 2, 300), dB=True, label="$L(s)$")

wc, pm, ts = CaclulateInfo(mag,phase,omega)
print(wc, pm, ts)
all_axes = plt.gcf().get_axes()



plt.sca(all_axes[0])
plt.title("Bode plot van $L(s)$ open lus")
plt.legend()
plt.scatter(wc,0)
plt.show()
