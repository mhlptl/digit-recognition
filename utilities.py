import numpy as np
import struct

def importData():
	images = ['train-images-idx3-ubyte', 't10k-images-idx3-ubyte']
	labels = ['train-labels-idx1-ubyte', 't10k-labels-idx1-ubyte']

	trainData = parseFiles(images[0], True)
	trainData = np.reshape(trainData, (-1, 784))
	trainLabels = parseFiles(labels[0])
	trainLabels = onehotEncoding(trainLabels, 10)
	testData = parseFiles(images[1], True)
	testData = np.reshape(testData, (-1, 784))
	testLabels = parseFiles(labels[1])
	testLabels = onehotEncoding(testLabels, 10)
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


def onehotEncoding(labels, outputs):
	encodedLabels = np.empty((len(labels), outputs), dtype=np.dtype(np.uint8))
	for label, index in enumerate(labels):
		zeros = np.zeros(outputs, dtype=np.dtype(np.uint8))
		zeros[label % 10] = 1
		encodedLabels[index] = zeros
	return encodedLabels