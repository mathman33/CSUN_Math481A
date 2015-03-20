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


def nfractal(K, pixel, eps, n):

#generates the newton fractal for a given polynomial

    r = 0.75; # ratio of number points along imaginary axis to number of points along real axis
    a = alpha + beta*1j

    limit = 1.5
    x_left = -limit;
    x_right = limit;
    y_bottom = -limit;
    y_top = limit;

    x = np.linspace(x_left, x_right, pixel)            # x / real coordinates
    y = np.linspace(y_bottom, y_top ,round(pixel*r))   # y / imaginary coordinates

    [Re, Im] = np.meshgrid(x,y)             # meshgrid
    C = np.zeros([round(r*pixel), pixel], complex)
    C = Re + Im*1.0j                           # matrix holding x and y coordinates or points on complex plane

    B = np.zeros([round(r*pixel), pixel], float)     # this matrix keeps track of speed of convergence to a root if B(i,j) is large, iteration diverges...
    Id = np.ones(B.shape);                  # matrix of ones

    #roots of polynomial to apply Newton's iteration to, in this case p(z) = z^4 - 1

    zeros = np.zeros(n, complex)

    for i in xrange(0, n):
        zeros[i] = math.cos((2*math.pi/n)*i) + math.sin((2*math.pi/n)*i)*1j

    Cn = C                        # initial guess for Newton's iteration

    # iterate the initial guess iter times, the iteration is applied to the
    # whole matrix using array element-by-element operations
    # second line inside the loop adds 1 to the entries of B if the
    # corresponding entry in matrix Cn remains close to a root of the
    # polynomial after the kth iteration

    for k in range(1,K):
        Cn -= a*(Cn**n - Id) / (n*Cn**(n-1))
        for i in xrange(0, n):
            B += (i+1.0)*(np.abs(Cn - Id*zeros[i]) < eps)
        if k % 10 == 0:
            print k

    #plt.matshow(B)
    #plt.caxis([0, K])
    plt.pcolormesh(x, y, B, cmap = color) # bone, copper, summer
    # plt.colorbar()
    plt.savefig("fractal_%d_%d_%d.png" % (K, pixel, n), format="png", dpi = 150)

    #axis equal;
    #axis off
    #frame = sprintf('fractal_movie/ffractal_%0.3d', n)
    #print ('-dpng', '-r75', frame)

    #clear B x y C Id Cn

nfractal(K, pixel, eps, n)

