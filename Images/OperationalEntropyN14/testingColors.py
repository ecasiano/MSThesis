import numpy as np
import matplotlib.pyplot as plt
import colors

orange = ["#ff8c00"]
blue = ["#4173b3"]

α = [0.6,0.2]
for cα in α:
    orange.append(colors.get_alpha_hex(orange[0],cα))
    blue.append(colors.get_alpha_hex(blue[0],cα))

x = np.linspace(-1,1,100)
for i,c in enumerate(orange):
        plt.plot(x,x**2+i,color=orange[i], linewidth=2)
        plt.plot(x,-x**2-i,color=blue[i], linewidth=2)

plt.show()
