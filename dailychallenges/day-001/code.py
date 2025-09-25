import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

no_itms = np.array([[1],[2],[3],[4],[5]])
prices = np.array([100,150,200,250,300])

model = LinearRegression()

model.fit(no_itms,prices)

princes_pred = model.predict(no_itms)

plt.scatter(no_itms,prices, color='blue')
plt.plot(no_itms,princes_pred,color='red')
plt.show()