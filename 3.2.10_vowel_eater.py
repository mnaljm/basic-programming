user_word = str(input("Please enter a word: ")).upper()

# For hver bokstav i ordet.
for letter in user_word:
    # Hvis bokstavet  IKKE er en vokal, så print det ellers fortsæt.
    if letter not in "AEIOU":
        print(letter)
    else:
        continue