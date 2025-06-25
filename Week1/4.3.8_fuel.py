def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784  # hvor mange gallons bruges på 100 km
    miles = 100000 / 1609.344       # hvor mange miles er 100 km
    return miles / gallons          # miles pr. gallon

def miles_gallon_to_liters_100km(miles):
    km_per_gallon = miles * 1.609344      # hvor mange km på 1 gallon
    liters_per_100km = 100 * 3.785411784 / km_per_gallon  # liter pr. 100 km
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
print(miles_gallon_to_liters_100km(23.5))
