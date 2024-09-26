# Opdracht 3 tekstfuncties
# Naam student: Kai Ketting
# Groep:

# Hier komt je code...
# opdr_3.py

def draw_tree():
    tree = [
        "    *",
        "   ***",
        "  ******",
        " ********",
        "***********",
        "    ***",
        "    ***",
        "    ***"
    ]
    return tree
def draw_five_trees():
    trees = draw_tree()
    for line in trees:
        print(line * 5)  # Vermenigvuldig de lijn met 5 voor vijf bomen

draw_five_trees()
