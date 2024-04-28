def primes_less_than_x():
    x = int(input("Enter a number to find all prime numbers less than it: "))
    if x <= 2:
        return [], x
    sieve = [True] * x  # Assume all numbers are prime initially
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime

    for start in range(2, int(x**0.5) + 1):
        if sieve[start]:
            for i in range(start*start, x, start):
                sieve[i] = False

    # Collecting prime numbers
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    count = len(primes)
    return primes, count, x

# Run the function and print the result
prime_numbers, count, x = primes_less_than_x()
print(f"\nThere are {count} primes less than {x}. They are:")
print(prime_numbers)


