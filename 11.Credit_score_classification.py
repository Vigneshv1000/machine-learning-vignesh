import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
np.random.seed(42)

data = {
    "Income": np.random.randint(20000, 120000, 500),
    "Loan": np.random.randint(50000, 300000, 500)
}

df = pd.DataFrame(data)

df["CreditScore"] = ((df["Income"] > 60000) & (df["Loan"] < 150000)).astype(int)

0
X = df[["Income", "Loan"]]
y = df["CreditScore"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Credit Score Accuracy:", accuracy)
