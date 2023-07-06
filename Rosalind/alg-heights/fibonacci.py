def Fibonacci_Loop(n):
    old = 1
    new = 1
    for itr in range(n - 1):
        tmpVal = new
        new = old
        old = old + tmpVal
    return new

def Pythonic_Fibonacci_Loop(n):
    old, new = 1, 1
    for itr in range(n - 1):
        new, old = old, old + new
    return new

print(Fibonacci_Loop(20))
print(Pythonic_Fibonacci_Loop(20))