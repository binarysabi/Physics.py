import numpy as np
import matplotlib.pyplot as plt

def harmonic_potential(x, k=1.0):
    return 0.5 * k * x**2

positions = np.linspace(-5,5,100)
energies = harmonic_potential(positions)

#Visualization of the function using the plotting functions, exact method shown in next episode
plt.plot(positions, energies, color='#00ffcc', lw=2)
plt.title(r'Harmonic Potential $V(x) = \frac{1}{2}kx^2$')
plt.xlabel('Position x')
plt.ylabel('Energy V(x)')
plt.show()