import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

data = {
    "Income": [30000,50000,70000,20000,90000],
    "LoanAmount": [200000,150000,100000,250000,50000],
    "LoanApproved": [0,1,1,0,1]
}

df = pd.DataFrame(data)

X = df[["Income","LoanAmount"]]
y = df["LoanApproved"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = GaussianNB()
model.fit(X_train, y_train)

print("Bank Loan Accuracy:", accuracy_score(y_test, model.predict(X_test)))
