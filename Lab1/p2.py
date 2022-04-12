#
# Implement the program to solve the problem statement from the second set here
# Find the smallest number m from the Fibonacci sequence, defined by f[0]=f[1]=1, f[n]=f[n-1] + f[n-2], for n > 2, larger than the given natural number n. (e.g. for n = 6, m = 8).
#

def smallfib(number):
    f = []
    f.append(1)
    f.append(1)
    i = 1
    while (f[i] <= number):
        f.append(f[i] + f[i - 1])
        i = i + 1
    m = f[i]
    return m

n = input("Give a value:" )
n=int(n)
print (smallfib(n))