fruits = [ ]

while True:

    fruit = input("Enter name of the fruit (or stop end):" )

    if fruit.lower() == "stop":
        break

    fruits.append(fruit)

print("Fruits in the list:")
for fruit in fruits:
    print(fruit)