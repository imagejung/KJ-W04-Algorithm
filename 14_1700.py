# 멀티탭 스케줄링 (그리디)

import sys
input = sys.stdin.readline

n,k = map(int, input().split()) # 멀티탭 구멍 n, 사용횟수 k
a = list(map(int, input().split()))

# 멀티탭 자리 미리 만들어 놓기
multitap = []
cnt = 0

for i in range(k):
    # 멀티탭에 사용할 기기가 이미 꽂혀있는 경우
    if a[i] in multitap:
        continue

    # 멀티탭에 자리가 있는 경우
    if len(multitap) != n:
        multitap.append(a[i])
        continue

    # 하나 뽑아야 하는 경우
    last_index = []
    flag = 0
    for j in range(n):
        # 언제 사용하는지 index 찾기
        if multitap[j] in a[i:]:
            last_index.append(a.index(multitap[j],i))
            flag += 1
        else:
            delete_index = j

    # 앞으로 사용 안하는 하나 뽑고 추가해줌
    if flag != n:
        multitap[delete_index] = a[i]
        cnt += 1

    # 전부다 사용하는거면 가장 나중에 사용하는거 뽑기 (last_index 값 가장 큰거)
    else:
        multitap.remove(a[max(last_index)])
        multitap.append(a[i])
        cnt += 1

print(cnt)

## git test
## git test!!