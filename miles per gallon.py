from random import randint
fuel = randint(10, 25)

miles = randint(100, 1000)

print("can travel at" + str(miles // fuel) + "miles per gallon")

print("car fule tank" + str(fuel) + "gallon")

print("the car can travel" + str(miles) + "miles on the tank")


veg = input("type name of vegetable")

if veg == "corn":
    print("the veg is corn")
else:
    print("the veg is not corn")

