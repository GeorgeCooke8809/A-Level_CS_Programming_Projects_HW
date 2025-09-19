def get_share(gold, pirates):
    per_pirate = gold // pirates
    captain = gold % pirates

    return f"Each pirate will get {per_pirate} units of gold each and the Captain will take {captain} units."

gold = int(input("Gold: "))
pirates = int(input("Pirates: "))

print(get_share(gold, pirates))