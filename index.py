## Source https://www.geeksforgeeks.org/secretary-problem-optimal-stopping-problem/

# Python3 Program to test 1/e law for
# Secretary Problem
from calendar import c
import random
import math

e = 2.71828

# To find closest integer of num.
def roundNo(num):
    if num < 0:
        return num - 0.5
    else:
        return num + 0.5


# Finds best candidate using n/e rule.
# candidate[] represents talents of n candidates.
def printBestCandidate(candidate, n):

    # Calculating sample size for benchmarking.
    sample_size = math.floor(roundNo(n / e))
    print(f"Sample size for benchmarking is {sample_size} out of {n}")

    # Finding best candidate in sample size
    best = 0
    for i in range(1, sample_size):
        if candidate[i] > candidate[best]:
            best = i

    # Finding the first best candidate that
    # is better than benchmark set.
    for i in range(sample_size, n):
        if candidate[i] >= candidate[best]:
            best = i
            break

    if best >= sample_size:
        print(
            "\nBest candidate found is",
            math.floor(best + 1),
            "with talent",
            math.floor(candidate[best]),
        )
    else:
        print("Couldn't find a best candidate")


# Driver code
n = 50

# generating random numbers for talent of candidate
candidate = [random.randint(1, 10) for i in range(n)]
print(candidate)
printBestCandidate(candidate, n)

# This code is contributed by mits
