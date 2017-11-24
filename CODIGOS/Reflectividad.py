import netCDF4
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.mlab import griddata

my_filename = './TAB130416002504_RAW4EU9.nc'
my_dataset = netCDF4.Dataset(my_filename, mode='r')
reflectividad = my_dataset.variables['reflectivity'][:]

def reflec(x,y):
    return reflectividad[x][y]

subreflec = []
ref_1_sweep = reflectividad[:]

rango = my_dataset.variables['range'][:]
tiempo = my_dataset.variables['time'][:]

subrango , subtiempo = [] , []

for x in range(0,664):
    subrango.append(rango[x])


for x in range(0,360):
    subtiempo.append(rango[x])

for x in range(0,360):
    aux = []
    for y in range(0,664):
        #aux.append(float(((ref_1_sweep[x][y])/200)**0.625))
        aux.append(ref_1_sweep[y][x])
    subreflec.append(aux)

'''
zi = griddata(subtiempo, subrango, subreflec , x, y, interp='linear')
CS = plt.contour(xi, yi, zi, 15, linewidths=0.5, colors='k')
plt.scatter(subtiempo, subrango, marker='o', s=5, zorder=10)
'''

fig = plt.figure()
cax = plt.imshow(subreflec)
plt.colorbar(cax, aspect = 15  )
plt.left(0.08)
plt.show()

#https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
