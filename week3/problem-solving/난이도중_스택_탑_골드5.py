# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493
import sys
input = sys.stdin.readline

n = int(input())
string = input().split()

top=[]
for index, value in enumerate(string):
    top.append((int(value), index+1))

result=[]
stack=[]
for cur_top in top:

    didExist = False
    while(stack):

        prev_top = stack[-1]
        if(prev_top[0] > cur_top[0]):
            result.append(prev_top[1])
            didExist = True
            break
        else:
            stack.pop()

    stack.append(cur_top)

    if(didExist == False):
        result.append(0)

print(' '.join(map(str, result))) #결과 출력 

