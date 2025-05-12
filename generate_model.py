import pickle
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[1, 2], [2, 3], [3, 4]])
y = [0, 1, 0]

model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
