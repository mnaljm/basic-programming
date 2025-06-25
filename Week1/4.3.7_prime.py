def is_prime(num):
    # Hvis num er mindre end eller lig med 1, er det ikke et primtal, på den måde håndterer vi også 0 eller negative tal
    if num <= 1:
        return False
    #  Vi ser om num kan deles med nogen tal fra 2 op til kvadratroden af num
    # Hvis det kan, er det ikke et primtal
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    # Hvis ingen tal delte num, er det et primtal
    return True

# demonstration af funktionen is_prime
# Netacad test
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
