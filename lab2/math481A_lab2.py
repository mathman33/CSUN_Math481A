import numpy as np
import matplotlib.pyplot as plt

DIRECTORY = "/Users/samuelfleischer/Desktop/School_Stuffs/FALL_2015/MATH481A/lab2"

def DivDiffs(x_data, function):
    n = len(x_data)
    DD = np.zeros([n,n+1])

    DD[:,0] = x_data
    DD[:,1] = function(x_data)
    for column in xrange(2,n+1):
        for row in xrange(0, n+1-column):
            num = DD[row + 1,column - 1] - DD[row,column - 1]
            denom = DD[row + column - 1,0] - DD[row,0]
            DD[row,column] = (num)/(denom)
    return DD

def makePolynomial(DD):
    def InterpolantDD(x):
        P = 0
        for i in xrange(0, len(DD[:,0])):
            term = 1
            for j in xrange(0, i):
                term *= (x - DD[j, 0])
            term *= DD[0, i+1]
            P += term
    
        return P
    return InterpolantDD

def makePolyTest(*zeros):
    def poly_test(x):
        prod = 1
        for z in zeros:
            prod *= (x - z)
        return prod
    return poly_test

def runge(x):
    return 1./(1.0 + (x**2))

def test(x):
    num = np.exp(x+1)
    denom = x + 5.0
    return num/denom

def problem_3():
    x_100 = np.linspace(-2.0,2.0,100)
    
    x_4             = np.linspace(-2.0,2.0,4)
    poly_1          = makePolyTest(0, -2, 2)
    DD_1            = DivDiffs(x_4,poly_1)
    interp_1        = makePolynomial(DD_1)
    p3_label        = "p_3(x)"
    p3_interp_label = "\overline{p_3}(x)"
    p3_error_label  = "|%s - %s|" % (p3_label, p3_interp_label)

    x_6             = np.linspace(-2.0,2.0,6)
    poly_2          = makePolyTest(0, -2, 2, -5, 5)
    DD_2            = DivDiffs(x_6,poly_2)
    interp_2        = makePolynomial(DD_2)    
    p5_label        = "p_5(x)"
    p5_interp_label = "\overline{p_5}(x)"
    p5_error_label  = "|%s - %s|" % (p5_label, p5_interp_label)

    plot_problem_3a(x_100, p3_label, p5_label, p3_interp_label, p5_interp_label, poly_1, poly_2, interp_1, interp_2)
    plot_problem_3b(x_100, p3_error_label, p5_error_label, poly_1, poly_2, interp_1, interp_2)

def plot_problem_3a(x_100, p3_label, p5_label, p3_interp_label, p5_interp_label, poly_1, poly_2, interp_1, interp_2):
    plt.figure()
    plt.plot(x_100, poly_1(x_100), "c", linewidth=2, label = r"$%s$" % p3_label)
    plt.plot(x_100, interp_1(x_100), ".k", label = r"$%s$" % p3_interp_label)
    plt.legend(loc=0)
    plt.savefig("%s/figures/problem3_a.png" % DIRECTORY, format = 'png')
    plt.close()

    plt.figure()
    plt.plot(x_100, poly_2(x_100), "c", linewidth=2., label = r"$%s$" % p5_label)
    plt.plot(x_100, interp_2(x_100), ".k", label = r"$%s$" % p5_interp_label)
    plt.legend(loc=0)
    plt.savefig("%s/figures/problem3_b.png" % DIRECTORY, format = 'png')
    plt.close()
    
def plot_problem_3b(x_100, p3_error_label, p5_error_label, poly_1, poly_2, interp_1, interp_2):
    plt.figure()
    plt.plot(x_100, abs(poly_2(x_100) - interp_2(x_100)), ".k", label = r"$%s$" % p5_error_label)
    plt.legend(loc=0)
    plt.savefig("%s/figures/problem3_b_error.png" % DIRECTORY, format = 'png')
    plt.close()

    plt.figure()
    plt.plot(x_100, abs(poly_1(x_100) - interp_1(x_100)), ".k", label = r"$%s$" % p3_error_label)
    plt.legend(loc=0)
    plt.savefig("%s/figures/problem3_a_error.png" % DIRECTORY, format = 'png')
    plt.close()

def problem_4():
    for n in [5, 10, 20, 30]:
        problem_4abcdef(n)
    problem_4g()    

def problem_4abcdef(n):
    x_n = np.linspace(-5.0, 5.0, n)
    
    DD_runge = DivDiffs(x_n, runge)
    interp_runge = makePolynomial(DD_runge)
    if n == 5:
        print DD_runge
    
    x_100     = np.linspace(-5.0, 5.0, 100)
    error_100 = abs(runge(x_100) - interp_runge(x_100))
    max_y     = max(error_100)
    max_index = list(error_100).index(max_y)
    max_x     = list(x_100)[max_index]
    
    runge_label        = "f(x)"
    runge_interp_label = "\overline{f_{%.02d}}(x)" % n
    runge_error_label  = "|%s - %s|" % (runge_label, runge_interp_label)
    
    plot_problem_4(n, x_100, runge_label, interp_runge, runge_interp_label, error_100, runge_error_label, max_x, max_y)

def problem_4g():
    intvl_1 = np.linspace(-5.0, -3.15, 20)
    intvl_2 = np.linspace(-3.0, 3.0, 11)
    intvl_3 = np.linspace(3.15, 5.0, 20)
    first_append = np.append(intvl_1, intvl_2)
    x_try = np.append(first_append, intvl_3)

    DD_try = DivDiffs(x_try, runge)
    interp_try = makePolynomial(DD_try)
    
    x_100 = np.linspace(-5.0, 5.0, 100)
    error_100 = abs(runge(x_100) - interp_try(x_100))
    max_y     = max(error_100)
    max_index = list(error_100).index(max_y)
    max_x     = list(x_100)[max_index]
    
    runge_label        = "f(x)"
    runge_interp_label = "\overline{f_{%.02d}}(x)" % 51
    runge_error_label  = "|%s - %s|" % (runge_label, runge_interp_label)
    
    plt.figure()
    plt.plot(x_100, runge(x_100), "c", linewidth = 2., label = r"$%s$" % runge_label)
    plt.plot(x_100, interp_try(x_100), ".k", label = r"$%s$" % runge_interp_label)
    plt.legend(loc=0)
    plt.savefig("%s/figures/problem4_g_51points.png" % DIRECTORY, format = 'png')
    plt.close()
    
    plt.figure()
    plt.plot(x_100, error_100, ".k", label = r"$%s$" % runge_error_label)
    plt.plot(max_x, max_y, c="c", marker="^", label = "max error: %.05f" % max_y)
    plt.ylim(0, 0.0018)
    plt.legend(loc=0)
    plt.savefig("%s/figures/problem4_g_error_51points.png" % DIRECTORY, format = 'png')
    plt.close()

def plot_problem_4(n, x_100, runge_label, interp_runge, runge_interp_label, error_100, runge_error_label, max_x, max_y):
    plt.figure()
    plt.plot(x_100, runge(x_100), "c", linewidth = 2., label = r"$%s$" % runge_label)
    plt.plot(x_100, interp_runge(x_100), ".k", label = r"$%s$" % runge_interp_label)
    plt.legend(loc=0)
    plt.savefig("%s/figures/problem4_d_%.3dpoints.png" % (DIRECTORY, n), format = 'png')
    plt.close()
    
    plt.figure()
    plt.plot(x_100, error_100, ".k", label = r"$%s$" % runge_error_label)
    plt.plot(max_x, max_y, c="c", marker="^", label = "max error: %.03f" % max_y)
    plt.legend(loc=0)
    plt.savefig("%s/figures/problem4_e_%.3dpoints.png" % (DIRECTORY, n), format = 'png')
    plt.close()

def main():
    problem_3()
    problem_4()

if __name__ == "__main__":
    main()