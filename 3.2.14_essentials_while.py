blocks = int(input("Enter the number of blocks: "))

# Vi starter højden på 0, fordi vi endnu ikke har bygget nogen lag.
height = 0
# Vi starter laget på 1, fordi det nederste lag i pyramiden altid kræver 1 klods.
layer = 1

# Så længe der er nok klodser til næste lag
while blocks >= layer:
    # Byg et lag mere
    height += 1
    # Træk brugte klodser fra
    blocks -= layer
    # Gå til næste lag (kræver én mere end før)
    layer += 1

print("The height of the pyramid:", height)
