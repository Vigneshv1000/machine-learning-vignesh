import csv, math

with open("tennis.csv") as f:
    data = list(csv.reader(f))[1:]

attrs = ["Outlook","Temp","Humidity","Wind"]
total = len(data)

yes = sum(1 for r in data if r[-1]=="Yes")
no = total - yes
entropy = -yes/total*math.log2(yes/total) - no/total*math.log2(no/total)

gains = []

for i in range(len(attrs)):
    e = 0
    for v in set(r[i] for r in data):
        s = [r for r in data if r[i]==v]
        y = sum(1 for r in s if r[-1]=="Yes")
        n = len(s)-y
        e += 0 if y==0 or n==0 else (len(s)/total)*(
            -y/len(s)*math.log2(y/len(s)) - n/len(s)*math.log2(n/len(s)))
    gains.append(entropy-e)
    print("Gain", attrs[i], "=", entropy-e)

root = attrs[gains.index(max(gains))]
print("\nRoot:", root)

sample = ["Sunny","Cool","High","Strong"]
print("Prediction:", "No" if sample[0]=="Sunny" else "Yes")
