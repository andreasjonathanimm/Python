import termcolor

from logic import *

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("Ballroom")
kitchen = Symbol("Kitchen")
library = Symbol("Library")
rooms = [ballroom, kitchen, library]

knife = Symbol("Knife")
revolver = Symbol("Revolver")
wrench = Symbol("Wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            termcolor.cprint(f"{symbol}: MAYBE", "yellow")
        else:
            termcolor.cprint(f"{symbol}: NO", "red")

knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench),
)

knowledge.add(Not(mustard))
knowledge.add(Not(kitchen))
knowledge.add(Not(revolver))

knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

knowledge.add(Not(plum))
knowledge.add(Not(ballroom))
check_knowledge(knowledge)