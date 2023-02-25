import numpy
from pomegranate import *

# Observation model for each state
sunny = DiscreteDistribution({
    "umbrella": 0.2,
    "no umbrella": 0.8
})

rainy = DiscreteDistribution({
    "umbrella": 0.9,
    "no umbrella": 0.1
})

states = [sunny, rainy]

# Transition model
transitions = numpy.array(
    [[0.8, 0.2], # Tomorrow's predictions if today is sunny
        [0.3, 0.7]] # Tomorrow's predictions if today is rainy
)

# Starting probabilities
start = numpy.array([0.5, 0.5])

# Create model
model = HiddenMarkovModel.from_matrix(transitions, states, start, state_names=["sunny", "rainy"])

model.bake()