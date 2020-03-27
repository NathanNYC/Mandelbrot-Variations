
# coding: utf-8

# In[34]:


#Mandelbrot fractal creation program 
#e.g. complex fractal shapes with recursive detail at increasing magnifications
#code adapted from example found @ docs.scipy.org/doc/numpy/user/quickstart.html

import matplotlib.pyplot as plt 
import numpy as np

def mbrot(h,w,maxit=125): #higher iterations = more complex edges; longer run times

    a,b=np.mgrid[-1.5:1.5:h*1j,-2:2.1:w*1j] #placement of object in plane
    c=a+b*1j
    d=c
    divtime=maxit+np.zeros(d.shape,dtype=float)

    for thing in range(maxit):
        d=d**2+c
        diverge=d*np.conj(d)>2**2
        div_now=diverge & (divtime==maxit)
        divtime[div_now]=thing
        d[diverge]=1

    return divtime

#sizing, visualization
plt.imshow(mbrot(1500,1500),cmap='winter') #cmap options: matplotlib.org/tutorials/colors/colormaps.html
plt.show()

