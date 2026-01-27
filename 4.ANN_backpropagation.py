from sklearn.neural_network import MLPClassifier
X = [[0,0],[0,1],[1,0],[1,1]]
y = [0,0,0,1]
model = MLPClassifier(hidden_layer_sizes=(2,),
                      activation='logistic',
                      learning_rate_init=0.5,
                      max_iter=1000)

model.fit(X, y)
print("Predictions:")
print(model.predict(X))
