import numpy as np
import struct
import matplotlib.pyplot as plt

def importData():
    images = ['train-images-idx3-ubyte', 't10k-images-idx3-ubyte']
    labels = ['train-labels-idx1-ubyte', 't10k-labels-idx1-ubyte']

    trainData = parseFiles(images[0], True)
    trainLabels = parseFiles(labels[0])
    testData = parseFiles(images[1], True)
    testLabels = parseFiles(labels[1])
    print(trainLabels[0])
    print(testLabels[0])
    return trainData, trainLabels, testData, testLabels

def parseFiles(filename, isImage=False):
    fp = open('./data/' + filename, 'rb')
    magicNumber, numItems = struct.unpack('>II', fp.read(8))
    if isImage:
        nRows, nCols = struct.unpack('>II', fp.read(8))
        buffer = fp.read(numItems * nRows * nCols)
        data = np.frombuffer(buffer, dtype=np.dtype(np.uint8).newbyteorder('>'))
        data = np.reshape(data, (numItems, nRows, nCols))
    else:
        buffer = fp.read(numItems)
        data = np.frombuffer(buffer, dtype=np.dtype(np.uint8).newbyteorder('>'))
    fp.close()
    return data

if __name__ == "__main__":
    importData()