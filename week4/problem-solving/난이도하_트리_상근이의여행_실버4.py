# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372
import sys
input = sys.stdin.readline

'''
사실상 넌센스 문제에 속한다.
어차피 모든 국가로 갈 수 있는 항공편이 있기에 n-1이 정답이 된다.
'''

t = int(input().strip())
result = []
for _ in range(t):
    n, m = map(int, input().split())

    result.append(n-1)
    for _ in range(m):
        input()

for r in result:
    print(r)
