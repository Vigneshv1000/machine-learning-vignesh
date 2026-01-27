import csv
with open("data.csv") as f:
    data = list(csv.reader(f))

data = data[1:]  
n = len(data[0]) - 1

S = data[0][:-1]
G = [['?'] * n]
for row in data:
    x = row[:-1]
    label = row[-1]

    if label == "Yes":
        for i in range(n):
            if S[i] != x[i]:
                S[i] = '?'
    else:
        for i in range(n):
            if S[i] != '?' and S[i] != x[i]:
                G.append(['?' if j != i else S[i] for j in range(n)])
print("Specific Hypothesis (S):", S)
print("General Hypotheses (G):")
for g in G:
    print(g)
