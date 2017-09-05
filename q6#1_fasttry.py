from sklearn.datasets import load_svmlight_file
import numpy as np
import sys
import math
import operator


def predict(Xtr, Ytr, Xts, k, metric=None):

    N, D = Xtr.shape

    assert N == Ytr.shape[0], "Number of samples don't match"
    assert D == Xts.shape[1], "Train and test dimensions don't match"

    if metric is None:
        metric = np.identity(D)

    Yts = np.zeros((Xts.shape[0], 1))
    for i in range(Xts.shape[0]):
        if i==0:
            f = open('myfile', 'a')
            f.write(str(Xtr))
            f.write('\n\n----------------\n\n')
            f.write(str(Xts[i]))
        
        M = Xtr - Xts[i]

        if i==0:
            f.write('\n\n--------MMMMMMMMMMMMMMMMMMMMMMMMMMMMM--------\n\n')
            f.write(str(M))
        

        dist = np.sqrt(np.sum(np.square(M), axis=1))
        

        if i==0:
            f.write('\n\n--------DDDDDDDDDDDDDDDDDDDDDDDDDDDDD--------\n\n')
            f.write(str(dist))
        #print("dist shape = ",dist.shape)
        #print(dist)
        

        neighbors = []
        for x in range(len(Ytr)):
            neighbors.append([int(Ytr[x]),dist[x]])
        #neighbors.sort(key=operator.itemgetter(1), reverse=True)
        #neighbors[np.argsort(neighbors.A[:, 1])]
        
        neighbors.sort(key=operator.itemgetter(1))
        if i==0:
            f.write('\n\n--------NNNNNNNNNNNNNNNNNNNNNNNNNNNN--------\n\n')
            f.write(str(neighbors))
        #f = open('myfile', 'a')

        # for x in range(k):
        #     f.write(str(neighbors))
        #     # f.write(str(neighbors[x][0]))  # python will convert \n to os.linesep
        #     # f.write(' -> ')
        #     # f.write(str(neighbors[x][1]))
        #     # f.write('\n')
        
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
                Yts[i] = 2
            else:
                Yts[i] = 3
        else:
            if c1 > c3:
                Yts[i] = 1
            else:
                Yts[i] = 3
        #print(c1,c2,c3)
        print('#',i,' -> ',int(Yts[i]),sep='')
        
        '''
        Predict labels for test data using k-NN. Specify your tuned value of k here
        '''
    #f.write('--------------------------------------------\n')  # python will convert \n to os.linesep


    #f.close()  # you can omit in most cases as the destructor will call it

    return Yts

def main(): 

    # Get training and testing file names from the command line
    traindatafile = sys.argv[1]
    testdatafile = sys.argv[2]
    k = int(sys.argv[3])
    print('started')
    # The training file is in libSVM format
    tr_data = load_svmlight_file(traindatafile)

    Xtr = tr_data[0].toarray();
    Ytr = tr_data[1];

    # The testing file is in libSVM format too
    ts_data = load_svmlight_file(testdatafile)

    Xts = ts_data[0].toarray();
    # The test labels are useless for prediction. They are only used for evaluation

    # Load the learned metric
 #   metric = np.load("model.npy")
    metric = None
    ### Do soemthing (if required) ###

    Yts = predict(Xtr, Ytr, Xts, k, metric)
    Yts_actual = ts_data[1]

    correct = 0
    for x in range(len(Yts)):
        if Yts_actual[x] == Yts[x]:
            correct += 1
    print('Accuracy for k = 10 => ',(correct/float(len(Yts))) * 100.0)

    # Save predictions to a file
	# Warning: do not change this file name
    np.savetxt("testY_k#10.dat", Yts)

if __name__ == '__main__':
    main()
