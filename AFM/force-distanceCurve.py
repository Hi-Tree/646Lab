import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.tseries.frequencies import get_period_alias

df = pd.read_csv("/home/physica/Downloads/FDC HOPG.csv", ";",header = None)
df = np.array(df).astype(float)

plt.plot(df[:,0], df[:,1])
plt.title("Force-Distance Curve HOPG")
plt.xlabel("Piezo Voltage [V]")
plt.grid()
plt.xticks(np.linspace(0,16,32).astype(int))
plt.yticks(np.linspace(-0.5,0.5,32))
plt.ylabel("Deflection Voltage [V]")
plt.show()