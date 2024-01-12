import random

# Generate a random 4-digit binary number (e.g., '1010')
random_binary = ''.join(random.choice('01') for _ in range(4))

# Convert the binary number to base 10
decimal_number = int(random_binary, 2)

print(f"Random Binary Number: {random_binary}")
print(f"Equivalent Decimal Number: {decimal_number}")