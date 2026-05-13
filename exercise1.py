# Use Ctrl + I to write some Python code
# Your instruction to the chatbot will be
# I am an amateur number theorist, and I am curious about special sequences of numbers. 
# I would like to write a couple of Python functions that tell me the following: 
# the nth number in the Fibonacci sequence, and the first ten prime numbers.

def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

def fibonacci_series(n): # I asked to create this function to test the actual series of Fibonacci numbers, not just the nth number.
    if n <= 0:
        raise ValueError("n must be a positive integer")
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def first_ten_primes():
    primes = []
    num = 2
    while len(primes) < 10:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes



if __name__ == "__main__":
    print("10th Fibonacci number:", fibonacci(10))
    print("First 10 Fibonacci numbers:", fibonacci_series(10))
    print("First ten prime numbers:", first_ten_primes())   


