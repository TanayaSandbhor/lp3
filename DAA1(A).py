import time

# --------------------------------------------------------
# Non-Recursive (Iterative) Fibonacci Series
# --------------------------------------------------------
def fibonacci_iterative_series(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series


# --------------------------------------------------------
# Recursive Fibonacci Function (to build series)
# --------------------------------------------------------
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_recursive_series(n):
    series = []
    for i in range(n):
        series.append(fibonacci_recursive(i))
    return series


# --------------------------------------------------------
# Main Program
# --------------------------------------------------------
n = int(input("Enter the number of terms: "))

# Measure time for iterative version
start_iter = time.time()
iter_series = fibonacci_iterative_series(n)
end_iter = time.time()

# Measure time for recursive version
start_rec = time.time()
rec_series = fibonacci_recursive_series(n)
end_rec = time.time()

# --------------------------------------------------------
# Display Results
# --------------------------------------------------------
print("\n===== Fibonacci Series (Non-Recursive / Iterative) =====")
print(iter_series)

print("\n===== Fibonacci Series (Recursive) =====")
print(rec_series)

print("\n===== Time Comparison =====")
print(f"Iterative approach time: {end_iter - start_iter:.6f} seconds")
print(f"Recursive approach time: {end_rec - start_rec:.6f} seconds")

print("\n===== Complexity Analysis =====")
print("Iterative → Time: O(n), Space: O(1)")
print("Recursive → Time: O(2^n), Space: O(n)")
