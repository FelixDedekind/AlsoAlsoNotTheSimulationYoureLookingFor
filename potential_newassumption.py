import matplotlib.pyplot as plt
import numpy as np
import cv2



epsilon0, epsilonR = 8.854*10**(-12), 1
epsilon = epsilon0*epsilonR
k = 1/(4*np.pi*epsilon)
U0 = 1



grid_im = cv2.imread('images/Capacitor_Electrodes.png')
xlen = ylen = 1
xres, yres = xlen/np.shape(grid_im)[0], ylen/np.shape(grid_im)[1]
electrode1 = electrode2 = []
initial_grid = np.zeros((np.shape(grid_im)[0],np.shape(grid_im)[1]))
x_grid, y_grid = np.shape(initial_grid)[0],np.shape(initial_grid)[1]
for ii in range(np.shape(grid_im)[0]):
    for jj in range(np.shape(grid_im)[1]):
        if(grid_im[ii,jj,0]!=0):
            electrode1.append([ii,jj])
            initial_grid[ii,jj]=U0
        elif(grid_im[ii,jj,2]!=0):
            electrode2.append([ii, jj])
            initial_grid[ii, jj] = -U0

def potential(r1,r2,U_temp):
    return k * U_temp/np.sqrt(sum([(r2[cc]-r1[cc])**2 for cc in range(len(r1))]))

def betterAndFasterThanNumpy(A,a):
    ii,jj = a[0],a[1]
    bool = False
    for kk in A:
        if(ii == kk[0] and jj == kk[1]):
            bool = True
    return bool

nx = ny = 5 #Number of image charge-distributions to each side
U = initial_grid
for ii in range(np.shape(U)[0]):
    print('Calculation at: ',round(ii/(np.shape(U)[0])*100,1), '%')
    for jj in range(np.shape(U)[1]):
        for xx in range(-nx, nx):
            for yy in range(-ny, ny):
                for kk in electrode1:
                    U[ii,jj] += potential([ii/xres*xlen,jj/yres*ylen], [nx*xlen + kk[0]/xres*xlen, ny*ylen + kk[1]/yres*ylen], U0)
                for kk in electrode2:
                    U[ii,jj] += potential([ii/xres*xlen,jj/yres*ylen], [nx*xlen + kk[0]/xres*xlen, ny*ylen + kk[1]/yres*ylen], -U0)


plt.contour(U)
plt.show()