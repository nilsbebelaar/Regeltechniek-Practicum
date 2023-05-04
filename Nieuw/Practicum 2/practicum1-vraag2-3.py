import numpy as np
import matplotlib.pylab as plt
import control


T = np.array([5.0])
N = np.array([1.0, 5.0])
H = control.tf(T,N)

print(H)
for w in [0, 1, 5, 10, 100,500]:
    Hw = control.evalfr(H, 1j * w)
    print("========================")
    print("W:",w,"H(jw):",Hw)
    print("W:",w,"|H(jw)|:",np.abs(Hw))
    print("W:",w,"args(H(jw)):",np.degrees(np.angle(Hw)))