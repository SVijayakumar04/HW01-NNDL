import numpy as np
from prob05_a import Df
from prob05_b import Dg
from prob05_c import Dh

def f(z_1,z_2):
    return z_1*z_2 + 1

def g(y_1,y_2):
    return np.array([[y_1+2*y_2],[4*y_1-y_2]])

def h(x_1,x_2,x_3):
    return np.array([[np.exp(x_1)*np.cos(x_2)+x_3],[np.exp(x_1)*np.sin(x_2)+x_3]])

def dfogoh(x_1,x_2,x_3):
    
    ### <--- START OF YOUR CODE
    
    # h(x) is (2,1)
    hx = h(x_1, x_2, x_3)
    h1 = hx[0, 0]
    h2 = hx[1, 0]

    # g(h(x)) is (2,1)
    gh = g(h1, h2)
    z1 = gh[0, 0]
    z2 = gh[1, 0]

    # chain rule: (1,2) @ (2,2) @ (2,3) -> (1,3)
    dfogoh = Df(z1, z2) @ Dg(h1, h2) @ Dh(x_1, x_2, x_3)

    ### END OF YOUR CODE --->

    return dfogoh

def main():

    x_1,x_2,x_3=0,0,0

    print(dfogoh(x_1,x_2,x_3))

if __name__ == "__main__":
    main()
