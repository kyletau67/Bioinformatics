#rabbit population with fibonacci sequence but the rabbits die after m months

def fibonacci(n,m):
    living = [1, 1]
    for i in range(2, n):
        # first reproduction
        tmp = living[i - 1] + living[i - 2]
        # then death begins occuring when m months occurs
        if i == m:
            tmp = tmp - 1
        if i > m:
            tmp = tmp - living[i - m - 1]
        # append total population into sequence
        living.append(tmp)
    print(living)
    return living[-1]


n = 97
m = 16


print(fibonacci(n,m))
