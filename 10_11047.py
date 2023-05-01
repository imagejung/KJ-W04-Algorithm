# 동전 0

# 입력부
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
coins = [int(input()) for i in range(n)]

cnt = 0
for i in range(n-1,-1,-1):
    # 하나씩 빼주는게 아닌 몫을 바로 구하기 가능
    # coins[i] 가 coins[i-1]의 배수이기 때문에
    # -> 큰 단위로 만들 수 있는금액은 무조건 작은금액으로도 만들 수 있는 수
    # -> 큰 수로 나눌 수 있으면 무조건 나누면 됨

    cnt += m // coins[i]
    m %= coins[i]

print(cnt)