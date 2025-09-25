# Linear Regression Example with sklearn

## Training Data
We have the following data:

```
X = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
```

👉 This follows the rule `y = 2x`.

---

## Code Example

```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])   # Features
y = np.array([2, 4, 6, 8, 10])            # Labels

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_)        # ~2
print("Intercept:", model.intercept_) # ~0
print("Predict x=6:", model.predict([[6]])) # ~12
```

---

## Why Predict x = 6?

- The model was trained on values 1–5.  
- Testing with `x = 6` checks if the model **generalizes to new data**.  
- This is the real power of Machine Learning: predicting unseen values.

👉 Example: If a student studies 1–5 hours (training data), we already know the scores.  
Now we predict for **6 hours** (new case).

---

## Bonus: Predict Multiple Values

```python
X_new = np.array([[6], [7], [10]])
print(model.predict(X_new))  # Predictions for new values
```

---

✅ Summary:  
- Train on known data  
- Test on unseen values  
- Linear Regression can generalize patterns
