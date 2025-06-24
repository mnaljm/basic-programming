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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
