# multiplication_table.py

# Prompt User for a Number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table
for i in range(1, 11):  # Loop from 1 to 10
    print(f"{number} * {i} = {number * i}")
