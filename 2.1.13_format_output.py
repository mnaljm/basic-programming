# Ved at bruge escape karakteren kan vi lave printen af pilen på en linje
arrow_lines = [
    "        **        ",
    "       *  *       ",
    "      *    *      ",
    "     *      *     ",
    "    ***    ***    ",
    "      *    *      ",
    "      *    *      ",
    "      ******      "
]
for line in arrow_lines:
    print(line + "  " + line)

# Try removing a quote or parenthesis below to see the error:
# print("This will cause an error)

# Try changing print to Print:
# Print("Case matters in Python!")

# Try using apostrophes instead of quotes:
# print('This works too!')