def is_year_leap(year):
    # Genbruger logik fra 3.1.12_essentials-elif.py til at afgøre om et år er et skudår
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    # Sørger for at måneden er gyldig før vi gør andet
    if month < 1 or month > 12:
        return 0
    # Tjekker om måneden er januar, marts, maj, juli, august, oktober eller december
    # og returnerer 31 dage
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # Tjekker om måneden er april, juni, september eller november
    # og returnerer 30 dage
    elif month in [4, 6, 9, 11]:
        return 30
    # Tjekker om måneden er februar og afgør antallet af dage baseret på om året er et skudår
    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28

def day_of_year(year, month, day):
    # Tjekker om datoen er gyldig
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    # Brug datetime til at finde ugedagen og formatere datoen
    import datetime
    date_obj = datetime.date(year, month, day)
    # strftime bruges til at formatere datoen og finde ugedagen
    weekday = date_obj.strftime("%A")
    date_str = date_obj.strftime("%d.%m.%Y")
    # F-string bruges til at returnere datoen og ugedagen
    return f"{weekday} {date_str}"

print(day_of_year(2000, 12, 31))
print(day_of_year(2024, 2, 29))   # Leap year, valid Feb 29
print(day_of_year(2023, 2, 29))   # Non-leap year, invalid Feb 29 (should return None)
print(day_of_year(2021, 4, 31))   # April has 30 days (should return None)
print(day_of_year(2022, 1, 1))    # Start of year
print(day_of_year(2022, 12, 31))  # End of year
print(day_of_year(2022, 6, 15))   # Middle of year
print(day_of_year(2022, 0, 10))   # Invalid month (should return None)
print(day_of_year(2022, 5, 0))    # Invalid day (should return None)