"""
You are given a list of q queries, and for each query, an integer n is provided.
The task is to find how many numbers less than or equal to n have exactly 3 divisors.

Input: q = 1
          query[0] = 6
Output: 1
Explanation: There is only one number 4 which has exactly three divisors 1, 2 and 4 and less than equal to 6.

Input: q = 2
       query[0] = 6
       query[1] = 10
Output: 1
        2
Explanation: For query 1 it is covered in the example 1. query 2:There are two numbers 4 and 9 having exactly 3 divisors and less than
equal to 10.

Solution:

A number has just 3 divisors if it is the square of a prime number

For example: 4 = 2^2 can be divided by (1,2,4). Note that 2 is a prime number
In order to solve this we have to find how many prime numbers we have up to sqrt(n)
We can use the Sieve of Eratosthenes algorithm to find the prime numbers up to sqrt(n)
"""

import math
from typing import List


def find_prime_numbers(n: int) -> List[int]:

    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = [False, False]

    for i in range(2, int(math.sqrt(n)+1)):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    prime_nums = [i for i, v in enumerate(is_prime) if v]

    return prime_nums


def three_divisors(query: List[int]) -> List[int]:

    output = [0] * len(query)
    max_n = int(
        math.sqrt(max(query))
    )

    prime_nums = find_prime_numbers(max_n)

    for i in range(len(query)):
        n = query[i]
        j = 0
        while j < len(prime_nums):
            if prime_nums[j]*prime_nums[j] <= n:
                output[i] += 1
            else:
                break

            j += 1

    return output


if __name__ == "__main__":
    print(three_divisors([6, 10]))
