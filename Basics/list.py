fruits = ["apple'", "orange", "mango", "banana", "pinaple"]
print(fruits[2])

#Data manipulation

fruits = ["apple'", "orange", "mango", "banana", "pinaple"]
fruits.append("guava")
fruits.insert(3, "grapes")

#swap Values
fruits[0],fruits[2] = fruits[2], fruits[0]

fruits.sort()

fruits.reverse()

print(fruits)