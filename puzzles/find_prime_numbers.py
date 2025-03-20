"""
The Sieve of Eratosthenes Algorithm

Find all prime numbers up to n
1. Set all numbers up to n+1 to True

[True, True, True, True, True, True, True, True]

2. Then set 0 and 1 to False (they are not prime numbers)

[False, False, True, True, True, True, True, True]

3. Iterate over all numbers up to sqrt(n) (We just need to check sqrt(n) numbers)
    1. Set all multiples of i to False if its value is True

       For example, if i == 2 we have:
            [False, False, True, True, False, True, False, True]

[True, False, False, ]

"""

import math
from typing import List


def find_prime_numbers(n: int) -> List[int]:

    is_prime = [True] * (n+1)

    is_prime[0], is_prime[1] = [False, False]

    for i in range(int(math.sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    prime_nums = [i for i, v in enumerate(is_prime) if v == True]

    return prime_nums


if __name__ == "__main__":
    print(find_prime_numbers(15))









