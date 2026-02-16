import numpy as np

def dA2dt(t):
    
    ### <--- START OF YOUR CODE

    A = np.array([
        [t**2, t + 1],
        [t**3 + t + 3, 7]
    ], dtype=float)

    dA = np.array([
        [2*t, 1],
        [3*t**2 + 1, 0]
    ], dtype=float)

    dA2dt = dA @ A + A @ dA

    
    ### END OF YOUR CODE --->

    return dA2dt

def main():
    t = 1

    print(dA2dt(t))

if __name__ == "__main__":
    main()
