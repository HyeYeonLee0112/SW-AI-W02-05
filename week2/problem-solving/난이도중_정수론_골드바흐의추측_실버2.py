# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020
import math

t = int(input())
myList=[]
for _ in range(t):
    myList.append(int(input()))

def isPrime(num):
    if(num == 2):
        return True
    elif(num < 2 or num%2 == 0):
        return False
    
    for quotient in range(3, round(math.sqrt(num))+1, 2):
        if(num % quotient == 0):
            return False
        
    return True

def findPartition(num):

    #파티션 찾기
    SubtractiveNum = round(num/2)

    for start in range(SubtractiveNum, 1, -1):

        if(not isPrime(start)):
            continue
        
        n1 = start
        n2 = num - start
        if(isPrime(n2) == True):
            return n1, n2

for num in myList:
    a, b = findPartition(num)
    print(f'{a} {b}')

