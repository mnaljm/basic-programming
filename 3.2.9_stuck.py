secretWord = "chupacabra"

while True:
    # For at gøre det nemmere at gætte, konverterer vi ordet til små bogstaver så det passer med vores secretWord
    guess = input(str("Enter your guess: ")).lower()
    # Hvis brugeren gætter det hemmelige ord, afslut loopet med break
    if guess == secretWord:
        print("You've successfully left the loop.")
        break
    # Ellers, hvis brugeren gætter forkert, fortsæt loopet uden nogen besked.
    else:
        continue