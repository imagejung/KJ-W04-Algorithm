# 회의실 배정 (그리디)

import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

# 1) 먼저 끝나는 회의, 2) 끝나는 시간이 같다면 빨리 시작하는 회의 기준으로 정렬
# (1,2) 선택한 뒤 (2,2)도 선택 가능하도록 하기 위해서
a.sort(key = lambda x : (x[1], x[0]))

# 빨리 끝나는 회의를 우선으로 계속 집어넣어야 함 (빨리 끝나는게 최선, 그리디)
cnt = 1
end_time = a[0][1]
for i in range(1, n):
    if a[i][0] >= end_time:
        end_time = a[i][1]
        cnt += 1

print(cnt)