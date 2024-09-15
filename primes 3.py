import math
import multiprocessing
import time
import psutil
import os

def generate_small_primes(limit):
    """Generate all prime numbers up to a given limit using the sieve of Eratosthenes."""
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime

    for num in range(2, int(math.isqrt(limit)) + 1):
        if sieve[num]:
            sieve[num*num:limit+1:num] = [False] * len(range(num*num, limit+1, num))

    return [num for num, is_prime in enumerate(sieve) if is_prime]

def sieve_segment(args):
    """Sieve a segment using the list of small primes."""
    segment_start, segment_end, small_primes = args
    segment_size = segment_end - segment_start
    sieve = [True] * segment_size

    for prime in small_primes:
        # Find the minimum number in [segment_start, segment_end) that is a multiple of prime
        start_index = (-(segment_start % prime) % prime)
        if segment_start + start_index == prime:
            start_index += prime  # Skip marking the prime number itself

        # Mark multiples of prime in the segment
        for multiple in range(start_index, segment_size, prime):
            sieve[multiple] = False

    # Collect primes in this segment
    segment_primes = [segment_start + i for i, is_prime in enumerate(sieve) if is_prime and (segment_start + i) > 1]
    return segment_primes

def parallel_segmented_sieve(n, num_processes):
    """Compute all prime numbers less than n using a parallel segmented sieve."""
    limit = int(math.isqrt(n)) + 1
    small_primes = generate_small_primes(limit)

    # Determine segment size
    segment_size = max(int((n - limit) / num_processes), 1)
    segments = []
    for segment_start in range(limit, n, segment_size):
        segment_end = min(segment_start + segment_size, n)
        segments.append((segment_start, segment_end, small_primes))

    # Use multiprocessing to sieve each segment in parallel
    with multiprocessing.Pool(processes=num_processes) as pool:
        segment_primes_list = pool.map(sieve_segment, segments)

    # Combine small primes and segment primes
    all_primes = small_primes.copy()
    for segment_primes in segment_primes_list:
        all_primes.extend(segment_primes)

    # Ensure primes are sorted
    all_primes.sort()
    return all_primes

if __name__ == '__main__':
    # Start performance measurement
    start_time = time.perf_counter()
    start_cpu_time = time.process_time()
    process = psutil.Process(os.getpid())
    start_memory = process.memory_info().rss  # in bytes

    # Input from the user
    n = int(input("Enter a number to find all prime numbers less than it: "))
    num_processes = multiprocessing.cpu_count()  # Use all available CPU cores

    # Compute primes using parallel segmented sieve
    primes = parallel_segmented_sieve(n, num_processes)
    count = len(primes)

    # Output the result
    print(f"\nThere are {count} primes less than {n}. They are:")
    print(primes)

    # End performance measurement
    end_time = time.perf_counter()
    end_cpu_time = time.process_time()
    end_memory = process.memory_info().rss  # in bytes

    # Calculate performance metrics
    elapsed_time = end_time - start_time
    cpu_time = end_cpu_time - start_cpu_time
    memory_usage = (end_memory - start_memory) / (1024 * 1024)  # Convert to MB

    print(f"\nPerformance Metrics:")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
    print(f"CPU time: {cpu_time:.6f} seconds")
    print(f"Memory usage: {memory_usage:.6f} MB")
    input("Press Enter to exit...")
    
