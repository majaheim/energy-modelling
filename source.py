import scipy.io
import numpy as np
import matplotlib.pyplot as plt
mat = scipy.io.loadmat('PV_Einspeiseprofil.mat', squeeze_me = True)
print(mat)
np.transpose(mat)
#print(mat['Leistung_Vec_Temperatur_Temp'])
E = mat['Leistung_Vec_Temperatur_Temp']
#E = E.tolist()
print(E)

# test plot
x = np.arange(0, 35040)
# x = np.linspace(0, 35039, 35040)
# np.transpose(x)
print(x)


plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, E, color ="red")
plt.show()