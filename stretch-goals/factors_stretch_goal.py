# -*- coding: utf-8 -*-
def factors(number):
    # ==============

    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            if i != 1 and i != number:
                factors.append(i)

    if len(factors):
        return factors
    else:
        return str(number) + " is a prime number"

    # ==============


print(factors(15))  # Should print [3, 5] to the console
print(factors(12))  # Should print [2, 3, 4, 6] to the console
print(factors(13))  # Should print “13 is a prime number”
