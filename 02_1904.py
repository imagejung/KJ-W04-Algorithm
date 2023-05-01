# 01타일 (동적프로그래밍, 상향식)

import sys
n = int(sys.stdin.readline())

tile = [] #dp table
for i in range(1,n+1):
    if i == 1:
        num = 1
    elif i == 2:
        num = 2
    else:
        # 답안 저장마다 15746 나눠주지 않으면 메모리 초과
        # 나머지 연산 분배법칙 활용
        num = (tile[-1] + tile[-2]) % 15746
    tile.append(num)

print(tile[-1])