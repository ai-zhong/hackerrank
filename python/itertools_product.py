from itertools import product

# You are given a two lists A and B.
# Your task is to compute their cartesian product AXB.
# Example: A = [1, 2]; B = [3, 4]; list(product(A,B)) will equal to:
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
# NOTE: Use * to unpack product() directly.

print(*product([int(a) for a in input().split()],
               [int(b) for b in input().split()]))

