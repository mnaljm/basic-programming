user_word = str(input("Please enter a word: ")).upper()
word_without_vowels = ""

# For hver bokstav i ordet.
for letter in user_word:
    # Hvis bokstavet  IKKE er en vokal, så tilføj det til ordet uten vokaler, ellers fortsæt.
    if letter not in "AEIOU":
        word_without_vowels += letter
    else:
        continue
# Print ordet uten vokaler.
print(word_without_vowels)