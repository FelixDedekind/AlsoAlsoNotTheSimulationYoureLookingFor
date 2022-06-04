import matplotlib.pyplot as plt
import numpy as np
import cv2

# 2D

grid_im = cv2.imread('images/Capacitor_Electrodes.png')
electrode1 = electrode2 = []
initial_grid = np.zeros((np.shape(grid_im)[0],np.shape(grid_im)[1]))
x_grid, y_grid = np.shape(initial_grid)[0],np.shape(initial_grid)[1]
for ii in range(np.shape(grid_im)[0]):
    for jj in range(np.shape(grid_im)[1]):
        if(grid_im[ii,jj,0]!=0):
            electrode1.append([ii,jj])
            initial_grid[ii,jj]=1
        elif(grid_im[ii,jj,2]!=0):
            electrode2.append([ii, jj])
            initial_grid[ii, jj] = -1



def YEAH_LAPLACE(grid0):
    grid1 = grid0
    c = 0
    for ii in range(np.shape(grid0)[0]-2):
        for jj in range(np.shape(grid0)[1]-2):
            if(betterAndFasterThanNumpy(electrode1,[ii+1,jj+1]) or betterAndFasterThanNumpy(electrode2,[ii+1,jj+1])):
                continue
            grid1[ii+1,jj+1] = (grid0[ii+2,jj+1]+grid0[ii,jj+1]+grid0[ii+1,jj+2]+grid0[ii+1,jj])/4
    return grid1

def betterAndFasterThanNumpy(A,a):
    """checks if value a is in set A"""
    ii,jj = a[0],a[1]
    bool = False
    for kk in A:
        if(ii == kk[0] and jj == kk[1]):
            bool = True
    return bool


grid0 = initial_grid

iterationsteps = 100
for cc in range(iterationsteps):
    print('Calculation at: ', round(cc/iterationsteps*100), '%')
    grid1 = YEAH_LAPLACE(grid0)
    grid0 = grid1



levels = [-0.5, 1, 0.5]

plt.contour(grid0, 10)
plt.show()
