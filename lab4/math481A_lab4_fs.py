from __future__ import division

from math import exp, sin, cos, pi, log

WELCOME = """Welcome to Sam Fleischer's Lab #4."""
PROMPT = """
Which problem would you like to see?
        
        Type a number 1-6

        or to exit, type "exit"

--> """
AGAIN_PROMPT = """
Would you like to see another problem? (y/n) --> """
INVALID_INPUT = """
INVALID - Please enter an integer 1-6"""
GOODBYE = """
Goodbye!
"""


def irange(start, stop, step):
    r = start
    while r <= stop:
        yield r
        r += step


def header(string):
    l = len(string)
    h = "#"*l + "\n"
    return "\n\n" + h + string + "\n" + h


def trap_area(b_1, b_2, h):
    return (1/2)*(b_1 + b_2)*h


def comp_trap_rule(f, a, b, n):
    h = (b-a)/n

    y_values = [f(a + i*h) for i in irange(0, n, 1)]

    approx = 0
    for i in xrange(0, len(y_values) - 1):
        approx += trap_area(y_values[i], y_values[i+1], h)

    return approx


def rect_area(b, h):
    return b*h


def comp_mdpt_rule(f, a, b, n):
    h = (b-a)/n

    approx = 0
    for i in xrange(0, n):
        approx += rect_area(h, f(a + i*h + (1/2)*h))

    return approx


def simp_rule(f, a, b):
    return (2*rect_area(f((a+b)/2), (b-a)) + trap_area(f(a), f(b), (b-a)))/3


def comp_simp_rule(f, a, b, n):
    if n % 2 != 0:
        raise "Simpson's Rule requires 'n' to be even"
    h = (b-a)/n

    approx = 0
    for i in xrange(0, int(n/2)):
        approx += simp_rule(f, a+(2*i*h), a+((2*i+2)*h))

    return approx


def first_order_deriv_approx(f, x, h=1e-6):
    return (f(x+h) - f(x))/h


def second_order_deriv_approx(f, x, h=1e-6):
    return (f(x+h) - f(x-h))/(2*h)


def exp_4b(x):
    return exp(-2*(x**2))


def kin_cos(t):
    return cos(2*pi*t)


def kin_sin(t):
    return sin(2*pi*t)


def kinematics(x, y, t, dt=1.0e-6):
    x_vel = first_order_deriv_approx(x, t, dt)
    y_vel = first_order_deriv_approx(y, t, dt)
    vel = (x_vel, y_vel)

    x_acc = (x(t+dt) - 2*x(t) + x(t-dt))/(dt**2)
    y_acc = (y(t+dt) - 2*y(t) + y(t-dt))/(dt**2)
    acc = (x_acc, y_acc)

    return (vel, acc)


def problem_1():
    print header("PROBLEM 1")
    print "\nCOMPOSITE TRAPEZOIDAL RULE"
    for n in [10, 20, 50, 100, 200]:
        print "\n    n = %d" % n
        a = comp_trap_rule(sin, 0, pi, n)
        b = comp_trap_rule(cos, 0, pi, n)
        c = comp_trap_rule(sin, 0, (pi/2), n)
        d = comp_trap_rule(exp, 0, log(3), n)
        print "        a = %.10e" % a
        print "        b = %.10e" % b
        print "        c = %.10e" % c
        print "        d = %.10e" % d


def problem_2():
    print header("PROBLEM 2")
    print "\nCOMPOSITE MIDPOINT RULE"
    for n in [10, 20, 50, 100, 200]:
        print "\n    n = %d" % n
        a = comp_mdpt_rule(sin, 0, pi, n)
        b = comp_mdpt_rule(cos, 0, pi, n)
        c = comp_mdpt_rule(sin, 0, (pi/2), n)
        d = comp_mdpt_rule(exp, 0, log(3), n)
        print "        a = %.10e" % a
        print "        b = %.10e" % b
        print "        c = %.10e" % c
        print "        d = %.10e" % d


def problem_3():
    print header("PROBLEM 3")
    print "\nCOMPOSITE SIMPSON'S RULE"
    for n in [10, 20, 50, 100, 200]:
        print "\n    n = %d" % n
        a = comp_simp_rule(sin, 0, pi, n)
        b = comp_simp_rule(cos, 0, pi, n)
        c = comp_simp_rule(sin, 0, (pi/2), n)
        d = comp_simp_rule(exp, 0, log(3), n)
        print "        a = %.10e" % a
        print "        b = %.10e" % b
        print "        c = %.15e" % c
        print "        d = %.15e" % d


def problem_4():
    print header("PROBLEM 4")
    print "\nDERIVATIVE APPROXIMATIONS"
    for h in [0.1, 0.05, 0.01, 0.001]:
        print "\n    h = %.3f" % h
        a = first_order_deriv_approx(exp, 0, h)
        b = first_order_deriv_approx(exp_4b, 0, h)
        c = first_order_deriv_approx(cos, 2*pi, h)
        d = first_order_deriv_approx(log, 1, h)
        print "        a = %.10e" % a
        print "        b = %.10e" % b
        print "        c = %.10e" % c
        print "        d = %.10e" % d


def problem_5():
    print header("PROBLEM 5")
    print "\nDERIVATIVE APPROXIMATIONS"
    for h in [0.1, 0.05, 0.01, 0.001]:
        print "\n    h = %.3f" % h
        a = second_order_deriv_approx(exp, 0, h)
        b = second_order_deriv_approx(exp_4b, 0, h)
        c = second_order_deriv_approx(cos, 2*pi, h)
        d = second_order_deriv_approx(log, 1, h)
        print "        a = %.15e" % a
        print "        b = %.15e" % b
        print "        c = %.15e" % c
        print "        d = %.15e" % d


def problem_6():
    print header("PROBLEM 6")
    print "\nVELOCITY AND ACCELERATION APPROXIMATIONS"
    for t in [0, (1/4), (1/2), (3/4)]:
        print "\n    t = %.2f" % t
        for dt in [0.1, 0.05, 0.01]:
            print "\n        dt = %.2f" % dt
            (vel, acc) = kinematics(kin_cos, kin_sin, t, dt)
            print "            vel = (%.10e, %.10e)" % (vel[0], vel[1])
            print "            acc = (%.10e, %.10e)" % (acc[0], acc[1])


def main():
    problem = {
        "1": problem_1,
        "2": problem_2,
        "3": problem_3,
        "4": problem_4,
        "5": problem_5,
        "6": problem_6,
    }
    print header(WELCOME)

    while True:
        value = raw_input(PROMPT)
        try:
            int(value)
        except:
            if value.lower() == "exit":
                break
            else:
                continue

        if value not in problem:
            print INVALID_INPUT
        else:
            problem[value]()
            again = str(raw_input(AGAIN_PROMPT))
            if again.lower() == "y" or again.lower() == "yes":
                pass
            else:
                print GOODBYE
                break

if __name__ == "__main__":
    main()
