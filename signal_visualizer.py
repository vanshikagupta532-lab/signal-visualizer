import numpy as np
import matplotlib.pyplot as plt

# Generate time values
t = np.linspace(0, 2*np.pi, 1000)

# Generate sine wave
signal = np.sin(t)

# Plot
plt.plot(t, signal)

plt.title("Sine Wave Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()