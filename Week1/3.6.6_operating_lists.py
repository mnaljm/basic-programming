my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Fjerner duplikater fra listen ved at konvertere den til et sæt og derefter tilbage til en liste.
my_list = list(set(my_list))

print("The list with unique elements only:")
print(my_list)

