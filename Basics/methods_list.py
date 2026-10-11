pets = ["cat", "dog", "rabbit", "parrot"]
pets.append("otter")
pets.insert(3, "goat")
print(pets)

pets[1],pets[2] = pets[2], pets[1]
pets.sort()
print(pets)
pets.reverse()
print(pets)