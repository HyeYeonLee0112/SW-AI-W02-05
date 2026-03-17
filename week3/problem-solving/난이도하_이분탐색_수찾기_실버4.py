# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
import sys

n=int(sys.stdin.readline())
seen = list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target):

    left, right = 0, len(arr)-1

    while(left <= right):
        mid = (left+right)//2

        if(target > arr[mid]):
            left = mid+1
            
        elif(target < arr[mid]):
            right = mid-1
            
        else: #타겟 찾으면 true 반환
            return 1

    return 0 #다 돌고도 못찾으면 false반환

#seen리스트 정렬
seen.sort()

result=[]
for num in find:
    result.append(binary_search(seen, num))

for r in result:
    print(r)


