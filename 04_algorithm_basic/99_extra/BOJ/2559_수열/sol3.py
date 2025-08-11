#  슬라이딩 윈도우롤 써줘야 된대

import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

arr = list(map(int, input().split()))

window = sum(arr[:K])
max_sum = window

for i in range(K, N):
    window += arr[i]
    window -= arr[i-K]

    if window > max_sum:
        max_sum = window
print(max_sum)