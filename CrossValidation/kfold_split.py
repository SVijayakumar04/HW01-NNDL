import numpy as np

def kfold_split(x,y,K,kcurr):
    # Extracting number of samples in the data
    N = len(x)

    # Specifying the number of samples in a fold
    Nfold = int(np.floor(N/K))

    ### <--- START OF YOUR CODE

 
    start = kcurr * Nfold

    if kcurr == K - 1:
        end = N
    else:
        end = start + Nfold

    idxVal = np.arange(start, end)
    idxPreVal = np.concatenate((np.arange(0, start), np.arange(end, N)))


    ### END OF YOUR CODE --->

    x_preval = x[idxPreVal]
    y_preval = y[idxPreVal]

    x_val = x[idxVal]
    y_val = y[idxVal]

    return x_preval, y_preval, x_val, y_val
