import time as t

for i in range(5):
    # Vi bruger f-string til at formatere udskriften så vi kan inkludere variablen i teksten
    print(f"{i + 1} Mississippi")
    
    # Fra time bruger vi sleep-funktionen til at pause i ét sekund
    t.sleep(1)

# Når loopet skriver vi den endelige besked 
print("Ready or not, here I come!")