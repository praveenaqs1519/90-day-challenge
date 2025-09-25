from sklearn.linear_model import LinearRegression
import numpy as np

v1 = np.array([[1], [2], [3], [4], [5]])
v2 = np.array([2, 4, 6, 8, 10])
model = LinearRegression()
model.fit(v1, v2)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction for 6:", model.predict([[6]])[0])
