# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
import sys

# n = int(sys.stdin.readline())
# myList = list(map(int, sys.stdin.readline().split()))

# count = 0

# for num in myList:
#     if(num%2 != 0):
#         pass

# print(myList)

inputList = input().split()
x = float(inputList[0])
n = int(inputList[1])
#x, n = map(float, input().split())

def myPow(x, n):
    if n == 0:
        return 1

    #양수로 제곱하는 경우
    elif n > 0: 
        
        #짝수 승의 경우: 재귀로 깊이 줄이기??
        if(n%2 ==0):
            num = myPow(x, n/2) 
            return num * num
        
        #홀수 승의 경우: x * 짝수승
        else:
            num = myPow(x, (n-1)/2)

            return x *  num * num

    #음수로 제곱하는 경우
    else:
        #x는 역수 취해주기
        x = 1/x
        #print(x)

        #짝수 승의 경우: 재귀로 깊이 줄이기??
        if(n%2 == 0):
            num = myPow(x, abs(n)/2) 
            return num * num
        
        #홀수 승의 경우: x * 짝수승
        else:
            num = myPow(x, abs(n-1)/2)

            return x *  num * num

print(myPow(x, n))