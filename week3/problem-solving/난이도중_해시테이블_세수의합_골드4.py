# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

import sys
input = sys.stdin.readline

n = int(input())
u = []
for _ in range(n):
    u.append(int(input()))

u.sort()
#print(u)
sumSet = set()

# x + y = k - z
'''
i = x + y를 해시로 저장한 후
i = k -z를 그 해시에서 찾기
'''

#두 수의 합에 대해 set에 다 저장하기
for x in u:
    for y in u:
        sumSet.add(x+y)

#합에 대한 z, k의 경우의수를 이중for문으로 순회하며 찾기??
didFind = False
result = 0
for k in u[::-1]:
    for z in u[::-1]:
        if( (k-z) in sumSet):
            result = k
            didFind = True
            break
    
    if(didFind == True):
        break

print(result)