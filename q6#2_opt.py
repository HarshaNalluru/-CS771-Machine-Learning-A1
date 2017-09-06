from sklearn.datasets import load_svmlight_file
import numpy as np
import sys
import math
import operator


def predict(Xtr, Ytr, v, metric=None):

    N, D = Xtr.shape

    if metric is None:
        metric = np.identity(D)

    Yts = np.zeros( (int(Xtr.shape[0]),1001) )

    for i in range(v, v + int(0.1*Xtr.shape[0])):
        
        M = Xtr - Xtr[i]
        dist = np.sqrt(np.sum(np.square(M), axis=1))

        neighbors = []
        for x in range(0,v-1):
            neighbors.append([int(Ytr[x]),dist[x]])
        
        for x in range(v + int(0.1*Xtr.shape[0]),Xtr.shape[0]):
            neighbors.append([int(Ytr[x]),dist[x]])

        neighbors.sort(key=operator.itemgetter(1))
        
        for k in range(1,1001):
            #print('----------',k,'--------\n')
            c1=0
            c2=0
            c3=0
            for x in range(k):
                response = neighbors[x][0]
                if response == 1:
                    c1 += 1
                elif response == 2:
                    c2 += 1
                elif response == 3:
                    c3 += 1

            if c2 > c1:
                if c2 > c3:
                    Yts[i][k] = 2
                else:
                    Yts[i][k] = 3
            else:
                if c1 > c3:
                    Yts[i][k] = 1
                else:
                    Yts[i][k] = 3
        print('#',i,sep='')
    
    f = open('myfile_acc_set4#opt', 'a')
    f.write('------------------------')
    f.write(str(v))
    f.write('------------------------\n')


    for k in range(1,1001):
        correct = 0
        for x in range(v, v + int(0.1*Xtr.shape[0])):
            if Ytr[x] == Yts[x][k]:
                correct += 1
        acc = (correct/float(0.1*Xtr.shape[0])) * 100.0

        f.write('Accuracy for k = ')
        f.write(str(k))
        f.write(' => ')
        f.write(str(acc))
        f.write('\n')

    f.write('------------------------\n')
    f.close()
    '''
    Predict labels for test data using k-NN. Specify your tuned value of k here
    '''
    return 

def main(): 

    # Get training and testing file names from the command line
    traindatafile = sys.argv[1]
    print('started')
    # The training file is in libSVM format
    tr_data = load_svmlight_file(traindatafile)

    Xtr = tr_data[0].toarray();
    Ytr = tr_data[1];

    # Load the learned metric
    # metric = np.load("model.npy")
    metric = None
    ### Do soemthing (if required) ###
    for v in range(0,10):
        predict(Xtr, Ytr, v*int(0.1*Xtr.shape[0]), metric)

    # Save predictions to a file
	# Warning: do not change this file name
    np.savetxt("testY.dat", Yts)

if __name__ == '__main__':
    main()
