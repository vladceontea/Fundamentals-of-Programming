
"""
 Generate all subsequences of length 2n+1, formed only by 0, -1 or 1, such that a1 = 0, ..., a2n+1= 0 and |ai+1 - ai| = 1 or 2, for any 1 ≤ i ≤ 2n.
"""


def solution(list, n, k):
    for i in range(n):
        if list[i] == list[i+1]:
            return False
    if list[0] != 0:
        return False
    if n == k-1:
        if list[k-1] != 0:
            return False
    return True


def output(list):
    if list is not None:
        print(*list)


def morevalues(list):
    if list[-1] < 1:
        return 1
    return 0


def back_recursive(n, number_list, k):
    for i in range(-1, 2):
        number_list.append(i)
        if solution(number_list, n, k) is True:
            if n == k-1:
                output(number_list)
            else:
                back_recursive(n+1, number_list, k)
        number_list.pop(n)


def back_iterative(k):
    number_list = [-1]
    n = 0
    while n > -1:
        if morevalues(number_list):
            number_list[n] = number_list[n] + 1
            if solution(number_list, n, k) is True:
                if n == k-1:
                    output(number_list)
                else:
                    n = n + 1
                    number_list.append(-2)
        else:
            number_list.pop(n)
            n = n - 1


def start():
    k = 0
    while k == 0:
        k = int(input("The number of elements (odd positive number): "))
        if k % 2 == 0 or k < 0:
            k = 0
            print("Please enter an ODD POSITIVE value.")

    print("Recursive backtracking: ")
    back_recursive(0, [], k)

    print("Iterative backtracking: ")
    back_iterative(k)


start()
