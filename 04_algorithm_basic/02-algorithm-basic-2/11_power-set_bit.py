arr = [1,2,3]
n = len(arr)
subset = []

# 모든 경우의 수에 대래서 조회
# for idx in range(2**n):
for idx in range(1 << n):
    tmp_subset = []
    for j in range(n):
        '''
            idx = 0
            j = 0
            idx = 3
        '''