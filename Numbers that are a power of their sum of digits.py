# def sumdigits(n):
#     summ = 0
#     for digit in str(n):
#         summ += int(digit)
#
#     return summ

#
# def power_sumDigTerm(n):
#     numlist = []
#     z = 81
#     totalLength = 0
#
#     while totalLength < n:
#         zInList = False
#         y = 2
#         while 2 ** y <= z and not zInList:
#             x = 1
#             while x ** y <= z and not zInList:
#                 if x ** y == z and sumdigits(z) == x:
#                     numlist.append(z)
#                     zInList = True
#                     totalLength += 1
#                 x += 1
#             y += 1
#         z += 1
#
#
#     return numlist[-1] # n-th term of the sequence, each term is a power of the sum of its digits
#
# print(power_sumDigTerm(3))













# def sum_digits3(n):  # fastest way to sum digits (https://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python)
#    r = 0
#    while n:
#        r, n = r + n % 10, n // 10
#    return r
#
#
# def power_sumDigTerm(n):
#     j = 0
#     z = 81
#
#     while j < n:
#         a = sum_digits3(z)
#         for b in range(2, 20):
#             pow = a ** b
#             if pow > z:
#                 break
#             if pow == z:
#                 jthterm = z
#                 j += 1
#         z += 1
#
#     return jthterm



#
# def sum_digits3(n):
#    r = 0
#    while n:
#        r, n = r + n % 10, n // 10
#    return r
#
#
# def power_sumDigTerm(n):
#
#     j = 0
#
#     z = 81
#
#     while j < n:  # while we haven't found the nth term of the sequence...
#         a = sum_digits3(z)
#         c = a
#         for _ in range(2, 5):
#             c *= a
#             if c > z:
#                 break
#             if c == z:
#                 jthterm = z
#                 j += 1
#         z += 1
#
#     return jthterm



def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r


def power_sumDigTerm(n):

    j = 0

    z = 81

    max_digits_considered = 5
    max_power_considered = 5

    list_of_tuples = []

    index = 0

    for digit_sum in range(9*max_digits_considered):
        for power in range(max_power_considered):
            potential_answer = digit_sum ** power
            if potential_answer > 80:
                list_of_tuples.append((potential_answer, digit_sum))
                index += 1

    list_of_tuples.sort()  # list of tuples is now a list of potential answers in the form (answer, digitsum)

    for potential_tuple in list_of_tuples:
        number = potential_tuple[0]
        if sum_digits3(number) == potential_tuple[1]:
            jthterm = number
            j += 1
        if j == n:
            return jthterm



print(power_sumDigTerm(5))