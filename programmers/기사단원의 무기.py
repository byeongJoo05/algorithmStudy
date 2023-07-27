"""
처음엔 2중 for문을 사용해서 일일히 약수를 세서 풀었다.
하지만 그러니 시간초과가 나는 경우가 발생하게 된다.

답지를 확인하니 제곱근을 통해 문제를 풀면 되는 것을 알았다.
패턴은 다음과 같다.
10 = 1, 2, 5, 10 이란 약수를 갖는다. 이 약수는 1 * 10, 2 * 5 와 같이 곱셈을 통해 다른 한 쪽의 수를 추측할 수 있는 것이다.
근데 제곱수의 경우는? -> 같은 로직을 반복하되 제곱이 된다면 -1을 해주니 되었다.
"""

def solution(number, limit, power):
    answer = 0
    l = []
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):  # 제곱근을 통하여 약수 갯수 추출. 10 = [1, 2, 5, 10] 인데 1 * 10, 2 * 5도 가능
            if i % j == 0:  # 따라서 한 숫자를 알면 그에 따른 다른 약수도 알 수 있으므로
                cnt += 2  # 2씩 추가가 됨
                if j ** 2 == i:  # 16은 4 * 4도 가능함. 따라서 제곱수의 경우 -1 을 해줌
                    cnt -= 1

            if cnt > limit:
                cnt = power
                break

        l.append(cnt)
    return sum(l)