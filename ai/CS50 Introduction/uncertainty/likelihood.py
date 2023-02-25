from model import model

# Calculate probability of a given observation
# probability = model.probability([["none", "no", "on time", "attend"]])
probability = model.probability([["none", "no", "on time", "miss"]])

print(probability)