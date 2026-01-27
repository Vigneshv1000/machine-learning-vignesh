from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture
from sklearn.metrics import accuracy_score
import numpy as np

X, y = load_iris(return_X_y=True)

gmm = GaussianMixture(n_components=3)
gmm.fit(X)

labels = gmm.predict(X)

labels = np.choose(labels, [1,2,0])  
print("EM Algorithm Accuracy:", accuracy_score(y, labels))
