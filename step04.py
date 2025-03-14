import numpy as np
from step01 import Variable
from step02 import Square
from step02 import Function
from step03 import Exp

def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps)

f = Square()
x = Variable(np.array(2.0))
dy = numerical_diff(f, x)
print(dy)

def f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))

x = Variable(np.array(0.5))
dy = numerical_diff(f, x)
print(dy)

class AddOne:
    def __call__(self, x):
        return Variable(x.data + 1)

x = Variable(np.array(5)) 
y = AddOne()  
result = y(x)  
print(result.data)  

def g(x):
    A = Exp()
    B = Square()
    return B(Variable(1+A(x).data))

x = Variable(np.array(1))
dy = numerical_diff(g, x)
print(dy)