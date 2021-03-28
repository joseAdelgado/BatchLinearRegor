import numpy as np
import pandas as pd
import argparse

eta,t = 0.01, 0.00001  #optimal hyperparameters

#********Matrix Calculations***************
def mat(dataset):
    ds = np.genfromtxt(dataset,delimiter=',')

    x = ds[:,0:-1].reshape(-1, ds.shape[1]-1)
    ones = np.ones([x.shape[0],1])
    x = np.concatenate([ones, x],1)

    y = ds[:,-1].reshape(-1,1)

    w = np.zeros([1, x.shape[1]])

    return x, y, w

#********Calculating SSE********************
def sqrerror(x, y, w):    
    e = np.power(((x@w.T)-y),2)
    return np.sum(e)

#********Implementing Batch Linear Regression*************
def regressor(dataset,eta,t):
    x, y, w = mat(dataset)
    costmat,res=[],[]
    key=0
    while True:
        currres=[]
        currres.append(key)
        key += 1
        cost = sqrerror(x,y,w)
        for ol in w:
            for il in ol:
                currres.append(il)
        currres.append(cost)
        costmat.append(cost)
        res.append(currres)
        w = w-(eta)*np.sum((x@w.T-y)*x,axis=0) #Gradient Calculation 

        if key>1:
            if (costmat[-2]-costmat[-1]) <= t:
                break
    return res

#************Driver code*************************
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--data',
                       help='your_dataset.csv')

    parser.add_argument('--eta',
                       help='learning rate = 0.0001')

    parser.add_argument('--threshold',
                       help='threshold value = 0.0001')

    args = parser.parse_args()

    dataset = args.data
    learning_rate = float(args.eta)
    threshold = float(args.threshold)

    op=regressor(dataset,learning_rate,threshold)
    print(pd.DataFrame(op))