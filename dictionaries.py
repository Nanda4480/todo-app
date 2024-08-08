'''
vehicle = {"tata": "nexon", "ford":"figo", "huyndai":"I10", "honda":"jazz"}
popularity = {"all": "tata", "by few": "ford", "most": "hyundai", "some": "honda"}
number = {0: 10, 10: 100, 100: 1000}
print(vehicle["ford"])
print("i love " + vehicle["ford"] + " from ford" + " but is "+ popularity["most"])
print(number[0])
print("tata" in vehicle)
print(vehicle.keys())

for key in vehicle.keys():
    print(key)

print(vehicle.values())
for value in vehicle.values():
    print(value)

print(vehicle.items())
for item in vehicle.items():
    print(item)
for key, value in vehicle.items():
    print(key, value)

if "ford" in vehicle:
    print(vehicle["renault"])
else:
    print("no ford")
'''
'''
vehicles = {"tata": "nexon", "ford":"figo", "huyndai":"I10", "honda":"jazz", "kia": "zika"}
print(len(vehicles))
if "tata" in vehicles:
    print(vehicles["tata"])
else:
    print("no tata")
print(len(vehicles))
'''
ex_1 = {}.fromkeys("ABcd", "bonerowska4")
print(ex_1)

vehicles = {"tata": "nexon", "ford":"figo", "huyndai":"I10", "honda":"jazz", "kia": "zika"}
vehicles.pop("honda")
print(vehicles)
vehicles.popitem()
removed = vehicles.popitem()
print(removed)


for key, value in {}.fromkeys("rivers", "beautiul").items():
    print(key, value)


fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))
fast_food_items.popitem()
print(fast_food_items)

vehicles = {"tata": "nexon", "ford":"figo", "huyndai":"I10", "honda":"jazz", "kia": "zika"}
bikes = {"tvs": "excel"}
vehicles.update(bikes)
print(vehicles)

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
gamers = internet_celebrities.copy()
internet_celebrities.clear()
print(internet_celebrities)
print(gamers)

vehicles = {"tata": "nexon", "ford":"figo", "huyndai":"I10", "honda":"jazz", "kia": "zika"}
if "renault" not in vehicles:
    vehicles["renault"] = "logan"
print(vehicles)

vehicles.setdefault("MG", "Hector")
print(vehicles)

vehicles = ("tata", "nexon", "ford", "figo", "huyndai", "I10", "honda", "jazz", "kia", "zika")
count = 0
while count < len(vehicles):
    print(vehicles[count])
    count += 1

reverse = len(vehicles) - 1
while reverse >= 0:
    print(vehicles[reverse])
    reverse -= 1

#sets
vehicles = {"tata", "nexon", "ford", "figo", "huyndai", "I10", "honda", "jazz", "kia", "zika"}
bikes = {"tata", "nexon", "huyndai", "I10", "honda", "jazz", "kia", "zika"}
common = vehicles.intersection(bikes)
print(common)

common = vehicles - bikes
print(common)

VEHICLES = {char.upper() for char in "i learning python"}
print(VEHICLES)





