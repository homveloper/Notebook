import matplotlib.pyplot as plt
import numpy as np

def make_circle(c, r):
    theta = np.linspace(0, 2 * np.pi, 256)
    x = r * np.cos(theta)
    y = r * np.sin(theta)    
    return np.vstack((x, y)).T + c

c = np.array([2, 3])
r = 1.5

circle = make_circle(c, r)

plt.figure(figsize = (4,4))
plt.plot(circle[:,0], circle[:, 1], 'b-')
plt.grid()
plt.xlim(0,5)
plt.ylim(0,5)
plt.show()
