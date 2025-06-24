c0 = int(input("Enter a non-negative, non-zero integer: "))
if c0 <= 0:
    print("Input must be a non-negative, non-zero integer.")
else:
    steps = 0
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        print(c0)
        steps += 1
    print("steps =", steps)