"""
When is a number, z, made up of 2^i*3^j*5^k?
This does not mean any multiple of 2,3,5...
If we want to check if a number is made up of the above, here is one solution:
    while z is not 2, 3 or 5:
        divide z by 2, unless answer is not int, then
            divide z by 3, unless answer is not int, then
                divide z by 5, unless answer is not int, then
                    z is not hamming number

Hence proposed solution is to do the above for z until we reach nth term
"""


# def hamming(n):
#     j = 0
#     x = 1
#
#     while j != n:
#         z = x
#         while True:
#             if z % 2 == 0:
#                 z = z / 2
#             elif z % 3 == 0:
#                 z = z / 3
#             elif z % 5 == 0:
#                 z = z / 5
#             elif z == 1:
#                 j += 1
#                 x += 1
#                 break
#             else:
#                 x += 1
#                 break
#
#     return x-1
#
#
# print(hamming(12))

"""
Above works but takes too long
Instead try computing batch-by-batch, noting that the UB is ub (see wiki on regular numbers), then sort
Use lists
"""
import math



# The number of hamming numbers between 1 and N is bounded above by ub(N)
# eg. N=50. Thus the number of hamming numbers between 1 and 50 cannot exceed ub(50) numbers.
# so if we generate 50 numbers that are less than ub(50) we know that we have a complete set of hamming numbers between 1 and ub(50)
# thus we can sort that set to get the first ub(50) hamming numbers
# ie. after n numbers are between 1 and s we can sort to get the first ub(s) numbers
ub = lambda N : ((math.log((N*math.sqrt(30))))**3) / (6 * math.log(2) * math.log(3) * math.log(5))


# need to generate numbers until ub(x) of them are less than x, then sort
# repeat until the nth number is less than ub(x)


def hamming2(n):

    lst = []

    for k in range(0, math.ceil(5000 ** (1 / 5))):
        for j in range(0, math.ceil(5000 ** (1 / 3))):
            for i in range(0, math.ceil(5000 ** (1 / 2))):
                lst.append(2 ** i * 3 ** j * 5 ** k)

    lst.sort()

    return lst[n-1]


print(hamming2(199))
