# Prompt the user for an arithmetic expression
expression = input("Enter an arithmetic expression (x y z): ").strip()

# Split the expression into components
x, operator, z = expression.split()

# Convert x and z to integers
x = int(x)
z = int(z)

# Calculate the result based on the operator
if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    result = x / z
else:
    raise ValueError("Invalid operator")

# Output the result as a floating-point value formatted to one decimal place
print(f"{result:.1f}")