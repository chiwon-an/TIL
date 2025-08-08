import itertools
arr = [1, 2, 3]

print(tuple(itertools.product(arr, repeat=7)))  # 중복순열
# ((1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1))