# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
import sys
input = sys.stdin.readline

def create_graph(vertex, edges):

    #1. 딕셔너리 초기화
    graph = dict()
    for index in range(1, vertex+1):
        graph[index] = []

    #2. 딕셔너리 구성
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]

        #딕셔너리
        graph[v1].append(v2)
        graph[v2].append(v1)

    return graph

def count_by_dfs(graph, start):

    visited = [0 for _ in range(len(graph)+1)]
    cnt = -1 #start 컴퓨터 제외
    stack = []
    stack.append(start)
    visited[start] = True

    while(stack):
        fromV = stack.pop()
        cnt += 1

        for toV in graph[fromV]:
            if(not visited[toV]):
                stack.append(toV)
                visited[toV] = True

    return cnt

#입력
n = int(input().strip())
m = int(input().strip())
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))

#딕셔너리 연결리스트 구성
graph = dict()
graph = create_graph(n, edges)

#처리
print(count_by_dfs(graph, 1))

