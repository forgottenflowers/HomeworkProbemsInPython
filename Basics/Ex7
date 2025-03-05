# Example problem 7
# Write a function to return a list with all divisors of div within the
# sequence 1 to n that are also even. For example, divisors(n,
# div) with n being 30 and div being 13 would return 26 while n
# being 50 and div being 7 would return 14, 28, and 42.
#
# Write a version using a standard for-loop, a version using a list
# comprehension, a version using a lambda function and a
# numpy version. Speed differences? Test with different sizes of n.
import numpy as np


def even_divs1(n, div):
    out = []
    for i in range(1, n + 1):
        if i % div == 0 and i % 2 == 0:
            out.append(i)
    return out


def even_divs2(n, div):
    return [x for x in range(1, n + 1) if x % div == 0 and x % 2 == 0]


def even_divs3(n, div):
    return list(filter(lambda x: x % div == 0 and x % 2 == 0, range(1, n + 1)))


def even_divs4(n, div):
    out = np.arange(1, n + 1)
    return list(out[(out % 2 == 0) & (out % div == 0)])


n = 3000000
div = 13

# timeit even_divs1(n, div)
# timeit even_divs2(n, div)
# timeit even_divs3(n, div)
# timeit even_divs4(n, div)
