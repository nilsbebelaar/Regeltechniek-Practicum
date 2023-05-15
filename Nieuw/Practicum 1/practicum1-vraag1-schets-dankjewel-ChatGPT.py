import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 100)  # Time range
h = 2 * np.exp(3 * t)       # Impulse response

plt.plot(t, h)
plt.xlabel('Time')
plt.ylabel('Impulse Response')
plt.title('Impulse Response of the System')
plt.grid(True)
plt.show()
