# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

'''
초기의 접근(틀림)
먼저 정렬하고 리스트의 절반쯤에 큰수를 역으로 집어 넣는 것이다 
1 4 8 10 15 20 
1 20 4 15 8 10 
|1-20| + | 20-4 | + ... 
19 + 16 +11 +7 + 2

인사이트: 하나의 규칙을 찾아 최적해를 찾는 게 아님
=>리스트 개수가 작아서 모든 경우의 수에 대해서 완전 탐색 가능
리스트 순열에 대한 모든 경우의수의 합은 백트래킹으로 찾기
'''

import sys

#입력
n = int(sys.stdin.readline())
myList= list(map(int, sys.stdin.readline().split()))

#사용했는지 검사하는 bool 리스트: 사용하지 않음으로 초기화
used=[False] * n
maxSum = 0

#리스트 순열에 대한 경우의 수
def backtrack(selectedList, maxSum):

    #베이스 케이스: 6개의 순열을 다 채운 경우
    if(len(selectedList) == n):

        #채워진 리스트 확인
        #print(selectedList)

        curSum=0
        #주어진 식에 따라 계산하기
        for index in range(n-1):
            curSum += abs(selectedList[index] - selectedList[index+1])

        #이전 기록보다 합이 더 크면 갱신
        if curSum > maxSum:
            maxSum = curSum

        return maxSum

    #리스트 만들기
    for index in range(n):
        #사용하지 않은 수 고르기
        if not used[index]:

            #선택
            selectedList.append(myList[index])
            used[index] = True

            #탐색
            maxSum = backtrack(selectedList, maxSum)

            #취소
            used[index] = False
            selectedList.pop()

        #사용한 수 =>다음 인덱스로

    #이부분 솔직히 이해가 안감
    return maxSum

print(backtrack([], maxSum ))