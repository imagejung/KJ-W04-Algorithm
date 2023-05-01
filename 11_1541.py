# 잃어버린 괄호
# 그리디

import sys
a = list(input().split('-'))
ans = 0

# 처음 -가 나오기 전까지 + 값들 더해주기
first = list(a[0].split('+'))
for i in range(0, len(first)):
    ans += int(first[i])

# - 기준으로 괄호쳐서(묶어서) 빼주기
for i in range(1,len(a)):
    tmp = list(a[i].split('+'))
    for j in range(len(tmp)):
        ans -= int(tmp[j])

print(ans)
