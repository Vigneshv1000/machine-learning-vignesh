import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    "Year": [2015, 2016, 2017, 2018, 2019],
    "Mileage": [50000, 40000, 30000, 20000, 10000],
    "Price": [500000, 550000, 600000, 650000, 700000]
}

df = pd.DataFrame(data)

X = df[["Year", "Mileage"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LinearRegression()
model.fit(X_train, y_train)

print("Predicted Prices:", model.predict(X_test))
