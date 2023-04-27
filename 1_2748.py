# 피보나치 수 2 (동적 프로그래밍)

import sys
n = int(sys.stdin.readline())

# 피보나치 수열을 만들어줘서 답을 다 넣어줌.
# 재귀함수로 반복적으로 계산하는 것 보다 훨씬 빠름.
fibonacci = []
ans = 0
for i in range(n+1):
    if i == 0:
        ans = 0
    elif i == 1:
        ans = 1
    else:
        ans = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(ans)

print(fibonacci[-1])
