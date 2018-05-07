import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv ##multiplicative inverse for a matrix
import scipy
from scipy import signal
from scipy.signal import wiener
from numpy import array
from numpy import empty
def loadSignal(fileName):
    #Load given signal
    return np.loadtxt(fileName)

def kth_diag_indices(matrix, k, value):
    points=[]
    rows, cols = np.diag_indices_from(matrix)
    if k < 0:
        rows=rows[-k:]
        cols=cols[:k]
    elif k > 0:
        rows=rows[:-k]
        cols=cols[k:]
    else:
        rows=rows
        cols=cols

    for i in range(len(rows)):
        points.append((rows[i], cols[i]))
    for i in range (len(points)) :
        matrix[points[i]]=value
    return matrix

def signalFilteration(signals, c, sigma2v, filterOrder):
    #Build and apply your filter
    #signal = wiener(signal, mysize=29, noise=0.5)

    n=len(signals)
    a = empty([filterOrder, filterOrder])
    b = empty([filterOrder, 1])
    Ryy=empty([n,1])
    ##Filling Ryy for Entire Signal
    for i in range(n):
        temp =0
        i2=i
        for i2 in range (n):
            if  (i2-i) >=0 :
                #print signals[i2] ,'*',signals[i2-i] ,'=', signals[i2] * signals[i2-i]
                temp += signals[i2] * signals[i2-i]
        #print temp

        Ryy[i]=(1.0/n)* temp


    b = Ryy[:filterOrder]
    b[0] = b[0]-sigma2v
    tempo =Ryy[:filterOrder]
    #filling Diagonals
    for k in range (filterOrder):
        a=kth_diag_indices(a,k,tempo[k])
    for k in xrange (-filterOrder+1,0):
        a=kth_diag_indices(a,k,tempo[k*-1])

    a=np.linalg.inv(a)
    #a= (1/c) * a
    h =np.matmul(a, b)/c
    #signals=np.convolve(h, signals)
    signals =signal.convolve(signals.reshape(signals.shape[0], 1), h,"same")
    #print h
    #print h.shape , signals.shape
    #print Ryy
    #print b
    #np.set_printoptions(suppress=True)
    #print a
    print signals.shape
    return signals


if __name__=='__main__':
    #Model Parameters c and sigmav^2
    c = -3
    varV = 0.02
    # Let filter order is 3
    filtOrder = 3
    #Load distorted signal
    y = loadSignal('distorted_ECG.txt')
    #y =loadSignal('t.txt')
    n = np.array(range(len(y)))
    # Make it zero mean
    y -= np.mean(y)


    # Apply filter
    filteredSignal = signalFilteration(y,c,varV, filtOrder)

    # Show the result
    plt.figure('filtered and distorted signals')
    plt.xlim(0,len(n))
    plt.plot(n, filteredSignal,'b',label='Filtered Signal')
    plt.plot(n,y,'r',label='Distored Signal')
    plt.legend()
    # now load the original signal
    x = loadSignal('Original_ECG.txt')
    # Make it zero mean
    x -= np.mean(x)
    # Plot it with filtered one
    plt.figure("Original vs Filtered")
    plt.xlim(0,len(n))
    plt.plot(n,x,'b', label='Original Signal')
    plt.plot(n,filteredSignal,'g', label = 'filtered Signal')
    plt.legend()
    #Get the mean square error
    meanSqrErr = np.mean(np.sqrt((x - filteredSignal)**2))
    print(meanSqrErr)
    plt.show()

