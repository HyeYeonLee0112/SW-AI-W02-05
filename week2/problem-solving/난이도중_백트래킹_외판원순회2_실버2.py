# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971
import sys

#입력
numsOfCity = int(sys.stdin.readline())
costMatrix = [ list(map(int, sys.stdin.readline().split() )) 
        for _ in range(numsOfCity)]

visited = [False] * numsOfCity #방문 여부에 대한 리스트

minCost = sys.maxsize #가장 큰 값으로 설정

#visitList를 n+1개로 함
def backtracking(numsOfSelected, visitList, minCost):
    
    #모든 도시 다 방문한 경우, 계산
    if(numsOfSelected == numsOfCity):

        #방문하는 경로 출력
        #print(visitList)

        #원래 도시로 돌아오는 경로를 추가
        visitList.append(visitList[0])

        #경로에 따른 비용 계산
        curCost = 0
        for index in range(numsOfCity): 
            c = costMatrix[visitList[index]][visitList[index+1]]

            #갈 수 없는 경우(비용 0): 조기 반환
            if(c == 0):
                visitList.pop() #마지막
                return minCost

            #갈 수 있는 경우: 비용 추가
            curCost += c

        #경로 계산 완료 후, 이전 비용보다 더 작다면 갱신
        if(curCost < minCost):
            minCost = curCost 

        #경로 계산을 위해 append한 도시 빼기
        visitList.pop()

        return minCost

    #경로 찾기
    for city in range(1, numsOfCity): #1부터 시작하는 이유는 시작점을 0으로 고정해서
        #방문 안한 도시만 선택
        if not visited[city]:
            visitList.append(city) #경로에 도시 추가
            visited[city] = 1 #방문했다고 표시하기

            #탐색
            minCost = backtracking(numsOfSelected+1, visitList, minCost)

            #취소
            visitList.pop() 
            visited[city] = 0 #방문 안했다고 표시하기


    return minCost


#시작 도시를 0(A)으로 고정
visited[0] = 1
print(backtracking(1, [0, ], minCost))

