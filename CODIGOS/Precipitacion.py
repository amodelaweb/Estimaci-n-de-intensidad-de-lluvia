import netCDF4
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go
import plotly.plotly as py
import matplotlib.mlab as mlab
def polarToCartesiano(theta, dist):
    x = dist * np.cos(theta)
    y = dist * np.sin(theta)
    return (x, y)

my_filename = './TAB130416002504_RAW4EU9.nc'
my_dataset = netCDF4.Dataset(my_filename, mode='r')

reflectividad = my_dataset.variables['reflectivity'][:]
ref = reflectividad[:]
azimuth = my_dataset.variables['azimuth'][:]
az = azimuth[:]
rango = my_dataset.variables['range'][:]
rg = rango [:]
tiempo = my_dataset.variables['time'][:]

intensidad = []
ax , ay , vz = [],[],[]

for i in range(0,360):
    aux = []
    for j in range(0,664):
        z = float(((ref[i][j])/200)**0.625)
        x, y = polarToCartesiano(az[i], rg[j])
        ax.append(x)
        ay.append(y)
        vz.append(z)
        aux.append(z)
    intensidad.append(aux)

fig = plt.figure()


im = plt.imread("mapa.jpg") # Leerpath imagen que contiene la mano
implot = plt.imshow(im) #Ubicar la imagen en la grilla


cax = plt.imshow(intensidad, interpolation = 'none' )
plt.colorbar(cax, aspect = 10  )
plt.set_cmap('nipy_spectral')
plt.xlim((0,517))
plt.ylim((509,0))

plt.show()
