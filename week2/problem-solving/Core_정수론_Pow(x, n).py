# https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150

inputList = input().split()
x = float(inputList[0])
n = int(inputList[1])

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
