#
# Implement the program to solve the problem statement from the third set here
# Determine the n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,... obtained from the sequence of natural numbers by replacing composed numbers with their prime divisors, without memorizing the elements of the sequence.
#

n = input("The position of the element: ")
n=int(n)
if n==1:
    print(1)
elif n==2:
    print(2)
else:
    k=2
    i=3
    ok=1
    while (ok==1):
        j = i
        for d in range(2,i+1):
            if j%d==0:
                k=k+1
            while j%d==0:
                j=j//d
            if k==n and ok==1:
                print("The element is", d)
                ok=0
        i=i+1
