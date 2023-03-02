

daytrip_destinations = ['Las Vegas', 'Paris', 'New York City', 'Miami', 'Topeka', 'San Diego']

daytrip_resteraunts = ['Hell"s Kitchen', 'la crossiants', 'mcdonalds', 'applebees', 'carnival world buffet', 'crawfish shack', 'lakeside view seafood']

daytrip_transportation = ['E-scooter', 'Uber', 'Taxi', 'Bus', 'Car', 'Limo', 'Heliocopter', 'plane','Walking']

daytrip_entertainment = ['Laser tag', 'The gym, Hiking', 'Bingo palor', 'The casino', 'The bar or pub', 'Theater', 'Amusement Park']

import random 
destinations = random.choice(daytrip_destinations)
restaurant = random.choice(daytrip_resteraunts)
transportation = random.choice(daytrip_transportation)
entertainment = random.choice(daytrip_entertainment)



destinations_2 = random.choice(daytrip_destinations)
restaurant_2 = random.choice(daytrip_resteraunts)
transportation_2 = random.choice(daytrip_transportation)
entertainment_2 = random.choice(daytrip_entertainment)


daytrip = (f"{destinations} {restaurant} {transportation} {entertainment}")

print(daytrip)

endtrip = input("Did you like your daytrip y/n ")

new_daytrip =(f"{destinations_2} {restaurant_2} {transportation_2} {entertainment_2}")
while endtrip == "n":
    print(new_daytrip)
    break
else:
    print("Have a fun trip!")
