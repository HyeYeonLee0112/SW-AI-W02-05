"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
"""

def dfs_by_Recursion(graph, start, visited=None):
    """
    깊이 우선 탐색 (재귀)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    # TODO: visited가 None이면 초기화
    if(not visited):
        visited = [False] * len(graph)
    
    result=[] #방문 순서 리스트
    # TODO: 현재 정점 방문
    visited[start] = True
    result.append(start)
    
    # TODO: 인접한 정점들에 대해 재귀
    for v in graph[start]:
    ## 방문하지 않은 정점이면 재귀 호출
        if(not visited[v]):
            result.extend(dfs(graph, v, visited))
    
    
    return result

def dfs_by_Stack(graph, start, visited=None):

    #방문 경로 초기화
    if(not visited):
        visited = set()

    result=[] #방문 순서 경로 리스트

    #스택
    stack = []
    stack.append(start)
    visited.add(start)

    #스택이 빌때까지 반복
    while(stack):
        
        #최신 노드 추출 및 방문 경로에 저장
        vertex = stack.pop()
        result.append(vertex)

        #visited에 없는 인접 노드만 스택에 넣기
        for adjacent in graph[vertex]:
            if(adjacent not in visited):
                stack.append(adjacent)
                visited.add(adjacent)

    return list(visited)

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs_by_Stack(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


