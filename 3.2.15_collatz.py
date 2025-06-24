# Vi validere at input er et ikke-negativt, ikke-nul heltal
c0 = int(input("Enter a non-negative, non-zero integer: "))
if c0 <= 0:
    print("Input must be a non-negative, non-zero integer.")
else:
    # Vi laver en løkke, der fortsætter indtil c0 er 1 og tæller hvor mange trin det tager
    steps = 0
    # Indtil c0 er 1, skal vi følge blive ved
    while c0 != 1:
        # Hvis c0 er lige, dividerer vi det med 2
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            # Hvis c0 er ulige, ganger vi det med 3 og lægger 1 til
            c0 = 3 * c0 + 1
        print(c0)
        steps += 1
    print("steps =", steps)