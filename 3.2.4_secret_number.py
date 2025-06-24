secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Looper indtil brugeren gætter det hemmelige tal
while True:
    guess = int(input("Enter your guess: "))
    # Hvis brugeren inputter præcist det hemmelige tal, afslut spillet
    if guess == secret_number:
        print("Well done, muggle! You are free now.")
        # Break bryder loopet
        break
    # Ellers bliver brugeren sendt tilbage til starten af loopet
    else:
        print("Ha ha! You're stuck in my loop!")