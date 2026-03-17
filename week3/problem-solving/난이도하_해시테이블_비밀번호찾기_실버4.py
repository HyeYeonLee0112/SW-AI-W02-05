#https://www.acmicpc.net/problem/17219
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

memo={}
for _ in range(n):
    line = input().split()
    memo[line[0]]= line[1]

result=[]
for _ in range(m):
    address = input().strip()
    result.append(memo[address])

for pw in result:
    print(pw)