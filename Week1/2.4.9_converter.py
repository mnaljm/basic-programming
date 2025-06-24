# Definere variabler for avstand i kilometer og miles
kilometers = 12.25
miles = 7.38

# Konvertere miles til kilometer og kilometer til miles
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

# Udskrive resultaterne og runde dem til 2 decimaler
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
