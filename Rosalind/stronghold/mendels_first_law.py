k = 22
m = 25
n = 16


def mendels_first(k, m, n):
    pop = k + m + n
    return (k*m + m*k + k*n + n*k + 0.5*(m*n+n*m) + k*(k-1) + 0.75*m*(m-1))/((pop)*(pop-1))

print(mendels_first(k,m,n))
