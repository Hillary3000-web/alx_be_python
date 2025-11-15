# pattern_drawing.py

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Use while loop to iterate through each row
while row < size:
    # Use for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after finishing the row
    row += 1  # Increment row counter
