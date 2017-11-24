import netCDF4
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.mlab import griddata
from random import randint

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
        r= randint(0, 25)
        if r != 0:
            aux.append(ref_1_sweep[y][x])
        else:
            aux.append(float('nan'))
    subreflec.append(aux)

'''
zi = griddata(subtiempo, subrango, subreflec , x, y, interp='linear')
CS = plt.contour(xi, yi, zi, 15, linewidths=0.5, colors='k')
plt.scatter(subtiempo, subrango, marker='o', s=5, zorder=10)
'''


fig = plt.figure()
cax = plt.imshow(subreflec, interpolation = 'nearest', cmap='viridis')

plt.colorbar(cax, aspect = 'auto'  )

plt.show()
