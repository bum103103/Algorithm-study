N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: x[0])
max_idx = max(range(N), key=lambda x: arr[x][1]) # 가장 큰 y좌표 인덱스저장

current_max = arr[0][1]
area = 0

# 새로 접근한 x좌표의 y값이 이전보다 크다면, 이전까지 넓이를 계산한 후 y값을 업데이트한다.
for i in range(0, max_idx):
    if arr[i][1] > current_max:
        current_max = arr[i][1]
    area += (arr[i+1][0] - arr[i][0]) * current_max        

area += arr[max_idx][1]

for i in range(N-1, max_idx, -1):
    if arr[i][1] > current_max:
        current_max = arr[i][1]
    area +=(arr[i][0] - arr[i-1][0]) * current_max


print(area)    