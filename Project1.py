import math
import time

"""
Inputs:
- n: integer that determines the size of the problem
- a: list of numbers comprising floats or ints
- b: list of numbers comprising floats or ints
"""
def Project1(n, a, b):
    # this will hold the final sum we want to return
    total_sum = 0.0

    # j starts at 5
    j = 5.0

    # this outer loop keeps going until j is halfway to n
    while j < n / 2:
        # have to reset k to 5 every single time the outer loop runs
        k = 5.0

        # this inner loop runs until k hits n
        while k < n:
            # j and k are floats because of the sqrt multiplication, converting to int for indexing
            j_index = int(j)
            k_index = int(k)

            # make sure the indexes aren't out of bounds before we use them
            if j_index < len(a) and k_index < len(b):
                 # the main calculation part: multiply elements and add to the total
                total_sum += a[j_index] * b[k_index]

            # update k
            k = k * math.sqrt(2)

        # now update j for the outer loop
        j = math.sqrt(3) * j

    return total_sum

if __name__ == "__main__":
    # Testing for different values of N
    # n_values = [1000, 5000, 10000, 150000, 100000, 150000, 1000000, 1500000, 10000000, 15000000, 100000000, 150000000, 1000000000]
    n_values = [100000, 300000, 1000000, 3000000,10000000, 30000000, 100000000, 300000000, 500000000, 750000000]

    experimental_times = []
    runs_to_average = 50 # Number of times to run for each N

    for n_size in n_values:
        # Use a constant list to make each test as consistent as possible
        a_data = [1] * n_size
        b_data = [1] * n_size
        
        total_time_for_n = 0
        print(f"Running for N = {n_size} ({runs_to_average} times)...")
        
        # Run the function multiple times and sum the time
        for _ in range(runs_to_average):
            start_time = time.perf_counter()
            Project1(n_size, a_data, b_data)
            end_time = time.perf_counter()
            total_time_for_n += (end_time - start_time)
            
        # Calculate the average time
        average_time = total_time_for_n / runs_to_average
        experimental_times.append(average_time)
        print(f"-> Average time: {average_time:.8f} seconds")