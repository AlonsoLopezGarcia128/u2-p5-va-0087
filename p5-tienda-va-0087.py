# Alonso Lopez Garcia NC = 0087
import matplotlib.pyplot as plt
import numpy as np
num_mes = np.array([1, 2, 3, 4, 5, 6])
venta_mandados = np.array([0, 2000, 3500, 7000, 15000, 20000])
plt.plot(num_mes, venta_mandados,
         marker= "d", 
        markersize = 10,
        markerfacecolor = "#6A9437",
        markeredgecolor = "blue"
        ),

plt.show()
