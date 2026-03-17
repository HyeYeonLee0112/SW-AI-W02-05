# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
from collections import deque

n = int(input())
myList = list( num+1 for num in range(n))
myQueue = deque(myList)

def getLastCard(queue):
    while(len(queue) != 1):
        
        #맨위 카드 하나 버리기
        queue.popleft()
        #다음 위 카드는 밑에 넣기
        insertCard = queue.popleft()
        queue.append(insertCard)
    
    return queue.popleft()


print(getLastCard(myQueue))