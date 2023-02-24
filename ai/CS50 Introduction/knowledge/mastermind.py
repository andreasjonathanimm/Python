from logic import *

colors = ["red", "green", "blue", "yellow"]
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

knowledge = And()

# Each color has a position
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3")
    ))

# Only one position per color
for color in colors:
    for i in range(4):
        for j in range(4):
            if i != j:
                knowledge.add(
                    Implication(Symbol(f"{color}{i}"), Not(Symbol(f"{color}{j}")))
                )

knowledge.add(Not(Symbol("blue0")))
knowledge.add(Not(Symbol("red1")))
knowledge.add(Not(Symbol("green2")))
knowledge.add(Not(Symbol("yellow3")))

knowledge.add(Or(Symbol("red0"), Symbol("blue1"), Symbol("green2"), Symbol("yellow3")))

print(model_check(knowledge))