#
# Implement the program to solve the problem statement from the first set here
# For a given natural number n find the minimal natural number m formed with the same digits. (e.g. n=3658, m=3568).
#

def firstzero(list):
    i = 0
    while list[i] == 0:
        i = i + 1

    list[0] = list[i]
    list[i] = 0

n = input("Give a value: ")
n = int(n)
y = n
l = []
while y>0:
    l.append(y%10)
    y = y//10

l.sort()
firstzero(l)
m=0
for i in range(len(l)):
    m = m*10 + l[i]

print("The number is:", m)