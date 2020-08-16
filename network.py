from utilities import *


def sigmoid(z):
	"""
		sigmoid function to squish the inputs between 0 and 1\n
		does elementwise operation if the input is a vector or matrix
	"""
	return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
	"""
		the derivative of the sigmoid function
	"""
	return sigmoid(z) * (1 - sigmoid(z))

def crossEntropy(output):
	pass

def cost_derivative(output_activations, y):
	return output_activations - y


class NeuralNetwork():
	def __init__(self, sizes: list) -> None:
		"""
			initialization of the neural network\n
			the number of neurons in each layer is passed in as the input
		"""
		self.numLayers = len(sizes)
		self.sizes = sizes
		self.biases = np.asarray([np.random.randn(x, 1) for x in sizes[1:]])
		# self.biases = np.reshape(self.biases, (len(self.biases), 1))
		self.weights = np.asarray([np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])])
		# self.weights = np.reshape(self.weights, (len(self.weights), 1))

	def feedForward(self, activation):
		"""
			feed forward algorithm to create an activation vector
			using the activations from the previous layer, as well
			as the weights and bias from the current layer. Running
			the dot product through the sigmoid allows for the output
			to be squished between 0 and 1.
		"""
		activations = [activation]
		zs = []
		for(bias, weight) in zip(self.biases, self.weights):
			z = np.dot(weight, activation) + bias
			zs.append(z)
			activation = sigmoid(z)
			activations.append(activation)

		self.activations = activations
		self.zs = zs
		return activation

	def SGD(self, X_train: list, y_train: list, batch_size: int = 50, learning_rate: float = 0.001, epochs: int = 500):
		"""
			implementation of Stochastic Gradient Descent\n
			there are m training examples and 'n' features
		"""

		m, n = np.shape(X_train)
