# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
import sys
input = sys.stdin.readline

n = int(input())
arr=list(map(int, input().split()))

arr.sort()

result=[sys.maxsize, 0, 0]

#n-1한 이유는 마지막 원소의 짝은 없어서..
for index in range(n-1):

    left=index+1
    right=n-1
    mid = 0
    target = -arr[index]
    didFind = False


    #이분탐색, num과 가장 가까운 값 찾기
    while(left <= right):
        mid = (left+right)//2

        if(arr[mid] < target):
            left = mid+1
        elif(arr[mid] > target):
            right = mid-1
        else: #정확히 타겟을 찾은 경우
            result = [0, arr[index], arr[mid]]
            didFind = True
            break
    
    #합이 0인 조합을 찾으면 아예 종료
    if(didFind):
        break

    #경계인 좌우값에 대해 타겟에 더 가까운 조합 찾기

    #왼쪽 보기
    if(left < n):
        diff_left = abs(arr[left] + arr[index])

        #왼쪽 수가 더 가까운 경우
        if(result[0] > diff_left ):
            result = [diff_left, arr[index], arr[left]]

    #오른쪽 보기
    if(right > index):
        diff_right = abs(arr[right] + arr[index])

        #오른쪽 수가 더 가까운 경우
        if(result[0] > diff_right):
            result = [diff_right, arr[index], arr[right]]
        
print(result[1], result[2])