A, B = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * A
# (간격)B는 이미 정의되어있음

max_sum = float('-inf')
sum = 0

for i in range(A):
    if i == 0:
        prefix[i] = arr[i]
    else:
        prefix[i] = prefix[i - 1] + arr[i]

for i in range(B, A):  # B부터 시작 (예제에서는 2부터)
    sum = prefix[i] - prefix[i - B]
    max_sum = max(max_sum, sum)

print(max_sum)    




