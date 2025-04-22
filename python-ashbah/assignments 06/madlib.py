print("******Madlib*********")
# Input collection
adjective1 = input("Enter an adjective: ")
pluralNoun1 = input("Enter a plural noun: ")
pluralNoun2 = input("Enter another plural noun: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter another adjective: ")
animalSound = input("Enter an animal sound: ")
person1 = input("Enter a person’s name: ")
adjective3 = input("Enter another adjective: ")
animal = input("Enter an animal: ")
substance = input("Enter something sticky/slimy (e.g. slime, mud, glitter): ")
person2 = input("Enter another person’s name: ")
reaction = input("Enter a dramatic reaction (e.g. doomed, eaten, cursed): ")
adjective4 = input("Enter another adjective: ")
flyingAnimal = input("Enter a flying animal (e.g. parrot, bat): ")
valuableItem = input("Enter something valuable (e.g. compass, map, food): ")
sameItem = input("Repeat the valuable item: ")
creature = input("Enter a mysterious creature: ")
adjective5 = input("Enter another adjective: ")

# Madlib construction
madlib = f"""One sunny morning, a group of {adjective1} adventurers set off on a journey into the wild,
untamed Amazon jungle. They packed {pluralNoun1}, {pluralNoun2}, and a giant {noun}, just in case they
encountered a {adjective2} problem. As they walked through the dense jungle, they suddenly heard a
loud {animalSound}. "What was that?!" yelled {person1}, looking around nervously. Out of the trees, a
massive {adjective3} {animal} appeared, covered in {substance}. "This is it!" screamed {person2}, "We’re gonna
get {reaction}!" But just then, a {adjective4} {flyingAnimal} swooped down and stole their last bag of {valuableItem}!
"No! Not the {sameItem}!" cried the group. "We’ll never survive the jungle without it!" They quickly followed
the {creature} creature into the jungle, which led them to a {adjective5} waterfall."""

# Output the story
print("\nHere is your madlib story!\n")
print(madlib)
