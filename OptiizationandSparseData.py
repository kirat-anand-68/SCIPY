#OPTIMIZERS -> a type of group procedure or function help to solve the complex to complex things->
#Used to find either min value root etc. any formula of the function.
#Optimizing functions  they are widely used in machine learning algorithm
#Root of an equation-> x+cos(x) we have to find the value of x then we used the optimizers in scipy to
# get out the value of x.
#we will solve it via optimize.root functions
#THis Function  Takes two arg-> "fun" and x0.
#EXAMPLE->
#HERE WE WILL FIND THE ROOT OF THE EQUATION-> x+cos(x)
# from scipy.optimize import root
# from math import cos

# def eqn(x):
#     return x+cos(x)
# myroot=root(eqn,0)
# print(myroot.x)
#HERE WE WANT THE INFO ABOUT NOT HUST X BUT WHOLE ROOT

# def eqn(x):
#     return x+cos(x)
# myroot=root(eqn,0)
# print(myroot)

#MINIMIZING THE FUNCTION->
# high point->global maxima
# low point->local maxima or minima
#FINDING THE MINIMA
#we use scipy.optimize.minimize(),it uses three arguments->"fun",x0, and method.
# It also has some legal values "CG","BFGS","NEWTON-CG","l-BFGS-B","TNC","COBYLA","SLSQP".
#CALL-BACK-> Function called after each iteration after optimizations.->
#EXAMPLE OF ABOVE -> in which we minimize the function x^2+x+2

# from scipy.optimize import minimize
# def eqn(x):
#     return x**2+x+2
# mymin=minimize(eqn,0,method="BFGS")
# print(mymin)
#*******************************************DATA SPARSE*************************************************
#What is spares data-> data which is useless unused or waste data.like the elements that not carry any information->
# [1,0,2,3,8,6,7]-> only a number.
#Sparse data example=[1,0,2,0,3,4,0,0,0,0]. all are maximum zero as having most zeroes called sparse data.
#[2,5,6,7,8,9,2,4]-> gives some of the information this is called the dense array.
#How to work with sparse data -> csr csc ->scipy has function scipy.sparsedata.there are 2 matrix in this sparse.CSC(Compressed sparse column) CSR(compressed sparse row)
#CSR MATRIX-> HERE WE WILL CREATE THE CSR MATRIX FROM THE ARRAY->
import numpy as np
from scipy.sparse import csr_matrix
x=np.array([0,0,0,0,1,3,5,3,8])
print(csr_matrix(x))
#It underestimate the zero
#It give the position of the elements other than the zero
# Coords  Values
# (0, 4)   1
# (0, 5)   3
# (0, 6)   5
# (0, 7)   3
# (0, 8)   8
#SPARSE MATRIX METHOD->
import numpy as np
from scipy.sparse import csr_matrix
x=np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(x).data)

#what if we want to count the nonzeroes,we can do this with the via count_nonzero() method.
import numpy as np
from scipy.sparse import csr_matrix
x=np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(x).count_nonzero())

#FOR REMOVING THE ZERO ELEMENTS FROM THE MATRIX WE WILL ELIMINATE.ZEROS().
import numpy as np
from scipy.sparse import csr_matrix
x=np.array([[0,0,0],[0,0,1],[1,0,2]])
x_new=csr_matrix(x)
x_new.eliminate_zeros()
print(x_new)

#DEALING WITH THE DUPLICATE ENTERIES WITH THE DUPLICATES METHOD->
import numpy as np
from scipy.sparse import csr_matrix
x=np.array([[0,0,0],[0,0,1],[1,0,2]])
x_new=csr_matrix(x)
x_new.sum_duplicates()
print(x_new)

#CSC METHOD-> here we will convert crc to csc->
import numpy as np
from scipy.sparse import csr_matrix
x=np.array([[0,0,0],[0,0,1],[1,0,2]])
x_new=csr_matrix(x).tocsc()
print(x_new)
