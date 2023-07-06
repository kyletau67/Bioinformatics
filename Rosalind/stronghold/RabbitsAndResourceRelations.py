#rabbit population with fibonacci sequence

def fibonacci(n,k):
    """calculating the value of rabbits in nth generation when 1 pair begins producing k pairs of bunnies"""
    if n == 0:
        return 1
    while n > 0:
        totalpairs += fibonacci(n-1,k)
    return totalpairs

n = 5
k = 3

print(fibonacci(n,k))