# 숫자 받기

n = int(input())


numbers = [list(map(str, input().split())) for _ in range(n)]


answer = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            counter = 0

            if (a == b or b == c or c == a):
                continue

            for array in numbers:
                check = list(array[0])
                strike = int(array[1])
                ball = int(array[2])

                strike_count = 0
                ball_count = 0

                # 스트라이크 계산
                if a == int(check[0]):
                    strike_count +=1
                if b == int(check[1]):
                    strike_count +=1
                if c == int(check[2]):
                    strike_count +=1

                # 볼 계산기
                if a == int(check[1]) or a == int(check[2]):
                    ball_count +=1
                if b == int(check[0]) or b == int(check[2]):
                    ball_count += 1
                if c == int(check[0]) or c == int(check[1]):
                    ball_count +=1


                if strike != strike_count:
                    break
                if ball != ball_count:
                    break

                counter += 1

            if counter == n:
                answer += 1

print(answer)