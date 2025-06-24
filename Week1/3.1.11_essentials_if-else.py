income = float(input("Enter the annual income: "))

tax_relief = 556.02

# Hvis indkomsten er mindre end 85.528, beregn skat med 18% minus fradrag
if income < 85528:
    tax = income * 0.18 - tax_relief
# Ellers, hvis indkomsten er større eller lig med 85.528, brug anden formel
else:
    tax = 14839.02 + (income - 85528) * 0.32

# Hvis skatten er mindre end 0, sættes den til 0
if tax < 0:
    tax = 0

# Afrund skatten til nærmeste hele tal
tax = round(tax, 0)


print("The tax is:", tax, "thalers")
