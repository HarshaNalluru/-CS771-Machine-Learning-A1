from sklearn.datasets import load_svmlight_file
import numpy as np
import sys
import math
import operator


def predict(Xtr, Ytr, Xts, metric=None):

    N, D = Xtr.shape

    assert N == Ytr.shape[0], "Number of samples don't match"
    assert D == Xts.shape[1], "Train and test dimensions don't match"

    if metric is None:
        metric = np.identity(D)

    Yts = np.zeros((Xts.shape[0], 1))
    k = 1;
    for i in range(Xts.shape[0]):
        M = Xtr - np.matmul(np.ones(len(Xts[i])).T, Xts[i])
        dist = np.sqrt(np.sum(np.square(M), axis=1))
        
        #print("dist shape = ",dist.shape)
        #print(dist)
        neighbors = []
        for x in range(len(Ytr)):
            neighbors.append((int(Ytr[x]),dist[x]))
        neighbors.sort(key=operator.itemgetter(1), reverse=True)

        f = open('myfile', 'a')

        # for x in range(k):
        #     f.write(str(neighbors))
        #     # f.write(str(neighbors[x][0]))  # python will convert \n to os.linesep
        #     # f.write(' -> ')
        #     # f.write(str(neighbors[x][1]))
        #     # f.write('\n')
        
        for x in range(k):
            print(neighbors[x][0])

        classVotes = {}
        classVotes[1] = 0
        classVotes[2] = 0
        classVotes[3] = 0

        for x in range(k):
            classVotes[int(neighbors[x][0])] += 1

        if classVotes[3] > classVotes[2]:
            if classVotes[3] > classVotes[1]:
                Yts[i] = 3
            else:
                Yts[i] = 1
        else:
            if classVotes[2] > classVotes[1]:
                Yts[i] = 2
            else:
                Yts[i] = 1

        print('#',i,' -> ',Yts[i],sep='')
        
        '''
        Predict labels for test data using k-NN. Specify your tuned value of k here
        '''
    f.write('--------------------------------------------\n')  # python will convert \n to os.linesep


    f.close()  # you can omit in most cases as the destructor will call it

    return Yts

def main(): 

    # Get training and testing file names from the command line
    traindatafile = sys.argv[1]
    testdatafile = sys.argv[2]
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

    Yts = predict(Xtr, Ytr, Xts, metric)
    Yts_actual = ts_data[1]

    correct = 0
    for x in range(len(Yts)):
        if Yts_actual[x] == Yts[x]:
            correct += 1
    print('Accuracy for k = 1 => ',(correct/float(len(Yts))) * 100.0)
    # Save predictions to a file
	# Warning: do not change this file name
    np.savetxt("testY.dat", Yts)

if __name__ == '__main__':
    main()
