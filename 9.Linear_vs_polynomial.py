import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([1,4,9,16,25])


lin = LinearRegression()
lin.fit(X, y)
y_lin = lin.predict(X)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)
y_poly = poly_reg.predict(X_poly)

plt.scatter(X, y, color='red', label='Data Points')
plt.plot(X, y_lin, color='blue', label='Linear Regression')
plt.plot(X, y_poly, color='green', label='Polynomial Regression (degree 2)')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear vs Polynomial Regression')
plt.legend()
plt.show()

print("Linear Regression R2:", r2_score(y, y_lin))
print("Polynomial Regression R2:", r2_score(y, y_poly))
