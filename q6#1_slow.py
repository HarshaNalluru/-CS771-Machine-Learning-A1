from sklearn.datasets import load_svmlight_file
import numpy as np
import sys
import math
import operator

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def predict(Xtr, Ytr, Xts, metric=None):

    N, D = Xtr.shape

    assert N == Ytr.shape[0], "Number of samples don't match"
    assert D == Xts.shape[1], "Train and test dimensions don't match"

    if metric is None:
        metric = np.identity(D)

    Yts = np.zeros((Xts.shape[0], 1))
    k = 1;
    for i in range(Xts.shape[0]):
        distances = []
        length = len(Xts[i])-1
        for x in range(len(Xtr)):
            #dist = np.linalg.norm(Xts[i] - Xtr[x])
            dist = np.dot(Xts[i] - Xtr[x], Xts[i] - Xtr[x])
            #dist = euclideanDistance(Xts[i], Xtr[x], length)
            distances.append((Ytr[x], dist))
        distances.sort(key=operator.itemgetter(1),reverse=True)
        neighbors = []
        for x in range(k):
            neighbors.append((int(distances[x][0]),distances[x][1]))
        #neighbors = getNeighbors(Xtr, Xts[i], k)
        print('#',i,' -> ',neighbors[0][0],sep='')


        classVotes = {}
        classVotes[1] = 0
        classVotes[2] = 0
        classVotes[3] = 0

        for x in range(len(neighbors)):
            response = neighbors[x][0]
            if response == 1:
                classVotes[response] += 1
            elif response == 2:
                classVotes[response] += 1
            elif response == 3:
                classVotes[response] += 1

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
        
        '''
        Predict labels for test data using k-NN. Specify your tuned value of k here
        '''

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
