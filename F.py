from math import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt

class F:
    def __init__(self,n,m):
        self.n = n
        self.m = m

    def __call__(self,x):
        x_val=[]
        for i in x:
            x_val.append(sin(self.n*i)*cos(self.m*i))
        return x_val
u = F(2,-10)
v = F(-1,1)
x_values = np.linspace(0,2*pi,1000)

u_array=np.array(u(x_values))
v_array=np.array(v(x_values))

plt.plot(u_array,v_array)
plt.xlabel("u")
plt.ylabel("v")
plt.show()

