import math
from mpmath import mp
import numpy as np
import matplotlib.pyplot as plt


def machineEpsilon(func = float):
    machine_epsilon = func(1)
    while func(1) + func(machine_epsilon) != func(1):
        machine_epsilon_last = machine_epsilon
        machine_epsilon = func(machine_epsilon) / func(2)
    return machine_epsilon_last

def sgn(x):
    if x < 0.0:
        return -1.0
    else:
        return 1.0

def quadratic(a,b,c):
    if (b**2 - 4*a*c) < 0:
        return "Negative Discriminant"
    else:
        x1 = (-b - math.sqrt(b**2 - 4*a*c))/(2.0*a)
        x2 = (-b + math.sqrt(b**2 - 4*a*c))/(2.0*a)
        return x1, x2

def double_der(f, x, h):
    numer = f(x + h) - f(x - h)
    denom = 2*h
    return numer/denom

def alt_quad(a, b, c):
    numer1 = -b - sgn(b)*math.sqrt(b**2 - 4*a*c)
    denom1 = 2.0*a
    x_1 = numer1/denom1
    numer2 = c
    denom2 = a*x_1
    x_2 = numer2/denom2
    return x_1, x_2

def f(x):
    numer = 1.0
    denom = 1.0 + x
    return numer/denom

def parab(a_0, a_1, a_2):
    def f(x):
        return a_0 + (x)*a_1 + (x**2)*a_2
    return f

def quadratic_mp(a,b,c,n):
    mp.dps = n
    a = mp.mpf(a)
    b = mp.mpf(b)
    c = mp.mpf(c)
    b2 = mp.mpf(b*b)
    ac4 = mp.mpf(4*a*c)
    d = mp.mpf(b2-ac4)
    d = mp.sqrt(d)
    num1 = mp.mpf(-b-d)
    num2 = mp.mpf(-b+d)
    denom = mp.mpf(2.0*a)
    #print 'a = %0.10f \nb = %0.10f \nc = %0.10f \nb^2 = %0.10f \n4ac = %0.10f \nd = %0.10f \nnum1 = %0.10f \nnum2 = %0.10f \ndenom = %0.10f' % (a, b, c, b2, ac4, d, num1, num2, denom)
    x1 = mp.mpf(num1/denom)
    x2 = mp.mpf(num2/denom)
    return x1, x2


p1 = parab(1, (-5.0/6.0), (1.0/3.0))
p2 = parab(1.0, -1.0, 1.0)
p3 = parab((26.0/27.0), (-20.0/27.0), (8.0/27.0))

x = np.arange(0, 1.1, 0.1)
y1 = abs(f(x) - p1(x))
y2 = abs(f(x) - p2(x))
y3 = abs(f(x) - p3(x))
plt.figure()
plt.plot(x, y1, label = "|f(x) - p_1(x)|")
plt.plot(x, y2, label = "|f(x) - p_2(x)|")
plt.plot(x, y3, label = "|f(x) - p_3(x)|")
plt.legend(loc=0)
plt.savefig("/Users/samuelfleischer/Desktop/School_Stuffs/FALL_2015/math_481A_lab1_figure.png", format = 'png')
