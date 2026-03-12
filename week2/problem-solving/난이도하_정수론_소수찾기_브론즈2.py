# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
import sys
import math

n = int(sys.stdin.readline())
myList = list(map(int, sys.stdin.readline().split()))

count = 0

def isPrimeNum(num):
    if(num == 2):
        return True
    elif(num < 2 or num%2 == 0):
        return False
        
    for n in range(3, round(math.sqrt(num))+1, 2):
        if(num % n == 0): #나머지가 0이 아니면
            return False

    return True


for num in myList:
    if(isPrimeNum(num) == True):
        count+=1


print(count)
