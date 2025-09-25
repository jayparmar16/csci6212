import math
import time # Need this for the square root and timing functions

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
    n_values = [1000, 5000, 10000, 150000, 100000, 150000, 1000000, 1500000, 10000000, 15000000, 100000000, 150000000, 1000000000, 1500000000]

    # Loop through each N value to test it
    for n_size in n_values:
        print(f"--- Running for N = {n_size} ---")

        # Creating two lists of size n, filled with some numbers
        a_data = [2] * n_size
        b_data = [3] * n_size

        # 1. Record the time before calling the function
        start_time = time.time()

        # Call the function to do the calculation
        final_result = Project1(n_size, a_data, b_data)

        # 2. Record the time *after* the function finishes
        end_time = time.time()

        # 3. Calculate the difference to find the execution time
        elapsed_time = end_time - start_time

        print(f"The final sum is: {final_result}")
        # Print the elapsed time, formatted to 6 decimal places for readability
        print(f"Execution Time: {elapsed_time:.6f} seconds\n")