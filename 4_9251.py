# LCS (Longest Common Subsequence, 최장 공통 부분 수열)
# 동적프로그래밍

import sys
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

cache = [0] * len(b)

# 일차원 배열을 하나 만들어 놓고
# a문자열의 문자 하나를 뽑아(순서대로) b문자열을 쭉 돌며 같은 문자인지 비교
# 같으면 cache[j]보다 앞에 값중 가장큰값 +1 로 cache[j] 업데이트
for i in range(len(a)):
    cnt = 0
    for j in range(len(b)):
        if cnt < cache[j]:
            cnt = cache[j]
        elif a[i] == b[j]:
            cache[j] = cnt + 1

# 맥스값 출력
print(max(cache))