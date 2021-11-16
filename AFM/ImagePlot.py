import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_zlim3d(-8, 8)
z = pd.read_csv("/home/physica/Downloads/Sample_Res250px_Speed200pps-2_Lateral.csv", header = None)
Z = np.array(z)*115
X = np.arange(0, 250, 1, dtype=float)
Y = np.arange(0, 250, 1, dtype=float)
X, Y = np.meshgrid(X, Y)
cmap = plt.cm.get_cmap('viridis_r')
cmap.set_under(cmap(1.0))
surf = ax.plot_surface(X, Y, Z,cmap=cmap, 
                       linewidth=1, shade = True, antialiased=True)


fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()