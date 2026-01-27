training_data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]
hypothesis = None

for example in training_data:
        attributes = example[:-1]
        label = example[-1]

        if label.lower() == "yes":  
            if hypothesis is None:
                hypothesis = attributes.copy()
            else:
                for i in range(len(attributes)):
                    if hypothesis[i] != attributes[i]:
                        hypothesis[i] = "?"
print("Final Hypothesis:", hypothesis)

