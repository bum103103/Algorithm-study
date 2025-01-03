# 브루트 포스.
# 가능한 모든 경우의 수를 때려박자
# 그리고 조건에 맞다면 출력

# 문제1. 비밀번호(#1816)

# # 입력
# TC = int(input())
#
# # 계산 및 출력
# # 1000000보다 작고 2이상의 약수를 가진다면 틀린 비밀번호가 된다.
#
# for a in range(TC):
#     number = int(input())
#
#     for i in range(2, 1000001):
#         if number % i == 0:
#             print('NO')
#             break
#         if i == 1000000:
#             print('YES')
#
#


TC = int(input())

for _ in range(TC):
    number = int(input())
    for i in range(2, 1000001):
        if number % i == 0:
            print('NO')
            break
        if i == 1000000:
            print('YES')