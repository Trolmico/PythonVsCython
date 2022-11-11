from cyfunctionE import rbf_network
import numpy as np

D = 5
N = 1500
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10

rbf_network(X, beta, theta)