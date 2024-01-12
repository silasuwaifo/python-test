# Function to generate the first 50 Fibonacci numbers
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

# Sum the first 50 Fibonacci numbers
n = 50
fibonacci_sequence = generate_fibonacci(n)
fibonacci_sum = sum(fibonacci_sequence)

print(f"The sum of the first {n} Fibonacci numbers is: {fibonacci_sum}")
