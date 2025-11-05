# Practical No: 1
# 1. Fibonacci sequence using recursion
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

# Number of terms (example)
nterms = 10
if nterms <= 0:
    print("PLEASE ENTER A POSITIVE INTEGER")
else:
    print("FIBONACCI SEQUENCE (recursive):")
    for i in range(nterms):
        print(recur_fibo(i))

# 2. Fibonacci sequence using iteration (non-recursive)
def fibonacci_iterative(nterms):
    a, b = 0, 1
    sequence = []
    for _ in range(nterms):
        sequence.append(a)
        a, b = b, a + b
    return sequence

try:
    nterms = int(input("Enter the number of Fibonacci terms: "))
    if nterms <= 0:
        print("PLEASE ENTER A POSITIVE INTEGER")
    else:
        print("\nFIBONACCI SEQUENCE (iterative):")
        result = fibonacci_iterative(nterms)
        for num in result:
            print(num)

        # 3. Display Time and Space Complexity Info
        print("\nTime Complexity: O(n)")
        print("Explanation: The loop runs 'n' times, so it scales linearly with input size.")
        print("Space Complexity: O(n)")
        print("Explanation: We store 'n' Fibonacci numbers in a list, using linear space.")
except ValueError:
    print("INVALID INPUT! Please enter a valid integer.")

