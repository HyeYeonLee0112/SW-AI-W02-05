# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
import sys


t = int(sys.stdin.readline())
testcase = [ 
    list(sys.stdin.readline().split())
    for _ in range(t)]


result=[]
for num in range(t):

    myStr=""
    for myChar in testcase[num][1]:
        myStr += myChar*int(testcase[num][0])  
    
    result.append(myStr)

for i in range(t):
    print(result[i])