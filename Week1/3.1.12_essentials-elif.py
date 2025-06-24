year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    # Hvis tallet IKKE kan divides med 4, er det et almindeligt år
    if year % 4 != 0:
        print("Common year")
    # Hvis tallet IKKE kan divides med 100, er det et skudår
    elif year % 100 != 0:
        print("Leap year")
    # Hvis tallet IKKE kan divides med 400, er det et al
    elif year % 400 != 0:
        print("Common year")
    # Hvis intet af ovenstående, er det et skudår
    else:
        print("Leap year")
