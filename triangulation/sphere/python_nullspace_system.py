import numpy as np
from numpy import array
import math
import algopy as ap
from algopy import UTPM, exp
import sympy as sp
from sympy import sin, cos, Matrix, var
import scipy as sci

from sympy.abc import I, pi
I=1j

# variables
var('x, y, z')
var_names = Matrix([x, y, z])

pi_1_2,pi_1_3,pi_1_4,pi_2_2,pi_2_3,pi_2_4, = sp.symbols('pi_1_2,pi_1_3,pi_1_4,pi_2_2,pi_2_3,pi_2_4,')

proj = np.array([[pi_1_2,pi_1_3,pi_1_4,],[pi_2_2,pi_2_3,pi_2_4,]])


# Degrees of the equations
num_projections = 2
num_jac_equations = 3
num_randomized_eqns = 1
target_crit_codim = -1

f1=Matrix([x**2+y**2+z**2-1])

#Random Functions
r_11 = sp.symbols('r_11')

# functions
F_orig = sp.Matrix([ f1])

# randomization matrix
F_rand = F_orig

# Compute Jacobian
Jac = F_rand.jacobian(var_names)
J = np.concatenate((Jac, proj),axis=0)
J2 = sp.Matrix(J)

# determinant
new_eqn = J2.det()

# Opening the first output file
fo = open("derivative_polynomials_declaration","w")
mystr1 = "function "
fo.write(mystr1)
n = 0
while ( n < num_randomized_eqns):
	m = n + 1
	func_base_str = "f%i" % m
	n = n + 1
	if n != num_randomized_eqns:
		eol_str = ", "
	else:
		eol_str = ";\n"
	mystr2 = func_base_str + eol_str
	fo.write(mystr2)

n = 0
while (n < num_randomized_eqns):
	m = n+1
	func_decl_str = "f%i = " % m
	func_def_str = str(F_rand[n])
	n = n+1
	eol_str = ";\n"
	mystr3 = func_decl_str + func_def_str + eol_str
	fo.write(mystr3.replace("**","^"))
mystr4 = "function der_func;\n"
mystr5a = "der_func = "
mystr5b = str(new_eqn) 
mystr5 = mystr5a+mystr5b+";\n"
fo.write(mystr4)
fo.write(mystr5.replace("**","^"))
fo.close()

