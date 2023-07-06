#rabbit population with fibonacci sequence

def fibonacci(n,k):
    """calculating the value of rabbits in nth generation/month when 1 pair begins producing k pairs of bunnies"""
    parent, child = 1, 1
    for itr in range(n - 1):
        child, parent = parent, parent + (k*child)
    return child

n = 33
k = 4

print(fibonacci(n,k))