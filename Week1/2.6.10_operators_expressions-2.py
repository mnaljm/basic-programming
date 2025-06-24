hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Beregn sluttidspunktet
end_mins = mins + dura  # Læg varigheden til minutterne
end_hour = hour + end_mins // 60  # Læg timer til, hvis minutterne går over 60
end_mins = end_mins % 60  # Find de resterende minutter efter hele timer er taget ud
end_hour = end_hour % 24  # Hvis timerne går over 24, start forfra ved 0
print(f"End time: {end_hour:02}:{end_mins:02}")  # Udskriv sluttidspunktet i formatet TT:MM