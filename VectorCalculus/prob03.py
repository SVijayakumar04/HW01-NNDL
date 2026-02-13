import numpy as np

def dinvA(x):
    
    ### <--- START OF YOUR CODE

   

    A = np.array([
        [1, x**3 + 3],
        [x**4 + x**2 + 3, x**2 + 1]
    ], dtype=float)

    dA = np.array([
        [0, 3*x**2],
        [4*x**3 + 2*x, 2*x]
    ], dtype=float)

    Ainv = np.linalg.inv(A)
    divnA = -Ainv @ dA @ Ainv


    ### END OF YOUR CODE --->

    return dinvA

def main():
    x = 1

    print(dinvA(x))

if __name__ == "__main__":
    main()
