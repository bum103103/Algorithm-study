# 브루트포스 방식
A, B, C, D, E, F = map(int, input().split())

for x in range(-10000, 10001):
    for y in range(-10000, 10001):
        if A*x + B*y == C:
            if D*x + E*y == F:
                print(x,y)
                break



# # X와 y는 -10000 이상 10000 이하의 정수
#
# A, B, C, D, E, F = map(int, input().split())
#
#
# if A == D :
#     n1 = B - E
#     n2 = (C - F)/n1 # y
#     n3 = (C - (B * n2))/A # x
#     print(n3, n2)
#
# else:
#     n4 = A/D
#     n5 = B - (n4 * E)
#     n6 = C - (n4 * F)
#     n7 = n6/n5 # y
#     n8 = (C - B * n7)/A # x
#     print(n8, n7)
#
# # 분모가 0이 되는 상황은 해가 무수히 많거나 없는 경우가 될 수 있으므로 따로 처리 필요




