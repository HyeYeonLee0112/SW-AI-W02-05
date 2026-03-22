# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
import sys
input = sys.stdin.readline

def dfs_by_stack(matrix, visited):

    size = len(matrix)
    endX, endY = size-1, size-1 #도착지 좌표

    stack =[] #후보가 될 좌표 저장하는  스택
    stack.append([0, 0]) #초기 좌표 저장


    while(stack):

        x, y = stack.pop() #pop한 좌표로 위치 갱신
        visited[x][y] = True #방문 표시
        move = matrix[x][y] #현재 타일 위의 수
        
        #오른쪽으로 가는 경우
        deltaX = x + move 
        if(deltaX < size):

            if(matrix[deltaX][y] == -1):
                return True

            if(not visited[deltaX][y]):
                stack.append([deltaX, y])

        #아래로 가는 경우
        deltaY = y + move 
        if(deltaY < size):
            if(matrix[x][deltaY] == -1):
                return True

            if(not visited[x][deltaY]):
                stack.append([x, deltaY])


    return False


#입력
n = int(input().strip())
matrix = list()

#표 구성
for _ in range(n):
    matrix.append(list(map(int, input().split())))

#방문 여부
visited = [[False] * n
    for _ in range(n)] 

#게임 돌려서 출력
if dfs_by_stack(matrix, visited):
    print("HaruHaru")
else:
    print("Hing")