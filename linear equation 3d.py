import matplotlib.pyplot as plt
from matplotlib import cm

#returns number spaces evenly w.r.t
#interval

x_axis, y_axis = np.linspace(0, 20, 10)
np.linespace(0, 20, 10)

#create a rectangular grid out of
#two given one-dimensional arrays

X, Y =np.meshgrid(x_axis, y_axis)
#make a rectangular grid
#3-dimensional by calculating
