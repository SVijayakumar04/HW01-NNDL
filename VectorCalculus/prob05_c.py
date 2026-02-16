import numpy as np

def Dh(x_1,x_2,x_3):
    
    ### <--- START OF YOUR CODE
   
    ex1 = np.exp(x_1)
    Dh = np.array([[ex1*np.cos(x_2), -ex1*np.sin(x_2), 1],
                   [ex1*np.sin(x_2),  ex1*np.cos(x_2), 1]])

    ### END OF YOUR CODE --->

    return Dh

def main():

    x_1,x_2,x_3=0,1,1

    print(Dh(x_1,x_2,x_3))

if __name__ == "__main__":
    main()
