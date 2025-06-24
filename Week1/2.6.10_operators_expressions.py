x = float(input("Enter a value for x: "))
# Baseret på billedet kan vi se at det er en brøk med en indlejret brøk så defer bruger vi paranteser til at sikre at vi får den rigtige rækkefølge i udregningen.
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))
print("y =", y)