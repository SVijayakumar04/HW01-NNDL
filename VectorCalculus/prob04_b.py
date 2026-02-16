import numpy as np

def d2Bdt2(t):
    
    ### <--- START OF YOUR CODE

    D = -t**4 - t**3 + 6*t**2 - 4*t - 3
    Dp = -4*t**3 - 3*t**2 + 12*t - 4
    Dpp = -12*t**2 - 6*t + 12

    d2Bdt2 = (Dpp*D - Dp**2) / (D**2)

    ### END OF YOUR CODE --->

    return d2Bdt2

def main():
    t = 0

    print(d2Bdt2(t))

if __name__ == "__main__":
    main()
