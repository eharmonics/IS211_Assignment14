# Print Fibonacci series up to n using recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Driver Program
n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
# Print in a single line
for i in range(n):
    print(fib(i), end=" ")

print(" ")
