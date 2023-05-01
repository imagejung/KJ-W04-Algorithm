# 신입 사원

# 자기보다 성적이 둘다 높은 사람이 한 명 이라도 있으면 탈락
import sys
input = sys.stdin.readline

t = int(input())

# 테스트케이스 t만큼 반복
for i in range(t):
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    # 우선 서류성적 순으로 정렬
    a.sort()

    # 서류 1등은 무조건 합격 (서류에 대해선 자기보다 성적 좋은 사람x -> 합격)
    top = a[0][1]
    ans = 1
    for j in range(1,n):
        # 서류 차순위자는 상위자보다 면접 성적이라도 좋아야 함
        # (j for문을 돌며 이미 자기보다 서류 좋은 사람들과 비교하여, 면접성적이라도 더 좋아야함)
        if a[j][1] < top:
            top = a[j][1]
            ans += 1
    print(ans)
