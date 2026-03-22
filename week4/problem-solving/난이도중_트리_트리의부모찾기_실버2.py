# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
'''
먼저 연결관계를 전부 저장한 뒤
1번에서 DFS/BFS로 퍼져 나가며
처음 방문하는 쪽의 부모를 기록
'''
import sys
from collections import deque
input = sys.stdin.readline
    
n = int(input().strip())


graph = dict() #무방향 그래프
for edge in range(1, n+1):
    graph[edge] = []

#그래프 형성
for _ in range(n-1): 
    u, v = map(int, input().split())

    #연결관계 저장: dict를 이용해 무방향 그래프
    graph[u].append(v)
    graph[v].append(u)

#큐를 이용해 부모 관계 파악
result = [0]*(n+1) #결과 저장용 배열
queue = deque()
queue.append(1)

while(queue):
    parent = queue.popleft()
    for child in graph[parent]:

        #연결된 정점으로 1이 나오면 무시
        if(child == 1):
            continue

        #부모 배열 값이 없으면 탐색
        if (result[child] == 0):
            result[child] = parent #부모 업데이트
            queue.append(child) #큐에 추가

print('\n'.join(map(str, result[2:])))