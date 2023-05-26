def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(N):
    primes = []
    for num in range(2, N + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
N = int(input("Enter a number: "))
prime_numbers = generate_primes(N)
print("Prime numbers up to", N, "are:", prime_numbers)
