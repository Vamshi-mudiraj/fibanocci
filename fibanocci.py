def fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Taking input from the user
num_terms = int(input("Enter the number of terms: "))

# Generating and printing Fibonacci sequence
fib_sequence = fibonacci_sequence(num_terms)
print("Fibonacci sequence:")
print(fib_sequence)

