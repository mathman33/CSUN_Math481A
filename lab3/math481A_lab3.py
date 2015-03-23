import sys
import math
import numpy as np
import matplotlib.pyplot as plt

K = int(sys.argv[1])
pixel = int(sys.argv[2])
eps = eval(sys.argv[3])
n = int(sys.argv[4])
color = str(sys.argv[5])

if len(sys.argv) > 6:
    alpha = float(sys.argv[6])
    if len(sys.argv) > 7:
        beta = float(sys.argv[7])
    else:
        beta = 0
else:
    alpha = 1
    beta = 0


def roots_of_unity(n):
    zeros = np.zeros(n, complex)
    for i in xrange(0, n):
        zeros[i] = math.cos((2*math.pi/n)*i) + math.sin((2*math.pi/n)*i)*1j

    return zeros
    
def get_iteration(n, a, Id, zeros, eps):
    def iteration(Cn, B):
        Cn -= a*(Cn**n - Id) / (n*Cn**(n-1))
        for i in xrange(0, n):
            B += (i+1)*(np.abs(Cn - Id*zeros[i]) < eps)
        return (Cn, B)
    return iteration

def nfractal(K, pixel, eps, n):
#generates the newton fractal for a given polynomial

    r = 0.75
    a = alpha + beta*1j

    limit = 2.0

    x = np.linspace(-limit, limit, pixel)
    y = np.linspace(-limit, limit ,round(pixel*r))

    [Re, Im] = np.meshgrid(x,y)
    C = np.zeros([round(r*pixel), pixel], complex)
    C = Re + Im*1.0j

    B = np.zeros([round(r*pixel), pixel], float)
    Id = np.ones(B.shape)

    zeros = roots_of_unity(n)
    iteration = get_iteration(n, a, Id, zeros, eps)
    
    Cn = C
    
    for k in range(1,K):
        (Cn, B) = iteration(Cn, B)
        print k

    plt.pcolormesh(x, y, B, cmap = color) # bone, copper, summer
    # plt.colorbar()
    file_name = "fractal_%d_%d_%d.png" % (K, pixel, n)
    plt.savefig(file_name, format="png", dpi = 150)
    print file_name
nfractal(K, pixel, eps, n)
print"\a\a\a"

