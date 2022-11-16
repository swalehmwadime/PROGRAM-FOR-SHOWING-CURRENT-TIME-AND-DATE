 #python program to solve linear equation
#and return a 3D graph

#import the libraries
import numpy as np
x1, y1, z1, w1 = 1, -2, 3, 9

#take the input for equation -2
x2, y2, z2, w2 = -1, 3, -1, 6

#take the inputs for equation -3
x3, y3, z3, w3 = 2, -5, 5, 17

#create array for LHS variables
LHS= np.array([[x1, y1, z1],
               [ x2, y2, z2],
               [ x3, y3, z3] ]


)
#create another array for RHS variables
RHS= np.array([w1, w2, w3])

#apply linear algebra on any numpy
#array created and printing output
sol= np.linalg.solve(LHS, RHS)
print(sol)
import matplotlib.pyplot as plt
from matplotlib import cm

#returns number spaces evenly w.r.t
#interval

x_axis, y_axis,  = np.linspace(0, 20, 10), np.linspace(0, 20, 10)

#create a rectangular grid out of
#two given one-dimensional arrays

X, Y =np.meshgrid(x_axis, y_axis)
#make a rectangular grid
#3-dimensional by calculating z1, z2,z3
Z1 = (w1-x1*X-y1*Y)/z1
Z2 = (w2-x2*X-y2*Y)/z2
Z3 = (w3+X-Y)/z3

#create 3D graphics and add an axes to the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#create a 3D surface plot
ax.plot_surface(X, Y, Z1, alpha=1,
               cmap=cm.Accent,
               rstride=100, cstride=100)
ax.plot_surface(X, Y, Z2, alpha=1,
                cmap=cm.Paired,
                rstride=100, cstride=100)
ax.plot_surface(X, Y, Z3, alpha=1,
                cmap=cm.Pastel1,
                rstride=100, cstride=100)


#draw points and make lines 
ax.plot((sol[0],), (sol[1],), (sol[2],),
         lw=2, c='k', marker='o',
         markersize=7, markeredgecolor='g',
         markerfacecolor='white' )

#set the label for x-axis, y-axis, and z-axis
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')                                

#display whole figure
plt.show()



