import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

arr = list(map(int, input().split()))

memo = [0] * (N-K+1)

for i in range(N-K+1):
    # temp = 0
    for j in range(i, i+K):
        memo[i] += arr[j]
    # memo[i] = temp

print(max(memo))

# max_temp = -float('inf')
# sum_temp = 0


# for i in range(N-K):
#     sum_temp += temp[i]

