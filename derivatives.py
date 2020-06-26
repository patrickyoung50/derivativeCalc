#this program will take the 1st and 2nd derivative of a
#given function and output it

import sympy as sym
from sympy import *
from sympy import core
init_printing(use_unicode=True)



def equationIn():
    global z, t, l, a, G, J, theta, inEq

    z, t, l, a, G, J, theta = sym.symbols('z t k a G J theta')
    inEq = ("((t*l*a)/(2*G*J))*(1+cosh(l/a))/sinh(l/a)*(cosh(z/a)-1)+(z/a)*(1-(z/l))-sinh(z/a)")

def derive1st2nd():
    deriv1 = sym.diff(inEq, z)
    simp1 = simplify(deriv1)

    print('The 1st derivative is ')
    pprint(simp1)

    deriv2 = sym.diff(deriv1, z)

    print('\nThe 2nd derivative is ')
    pprint(deriv2)

equationIn()
derive1st2nd()
