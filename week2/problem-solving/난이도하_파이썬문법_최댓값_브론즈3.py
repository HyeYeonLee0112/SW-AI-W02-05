# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562
import sys #인풋을 더 빠르게 하는 메서드를 지원하는 모듈

#list = sys.stdin.readline() #
myList = []

for line in sys.stdin: #입력 개수는 상수가 아님
    myList.append(int(line))  
    # strip메서드로 줄바꿈 문자 '\n'제거가 필요할 줄 알았으나
    # int()가 자동으로 공백과 개행문자 제거

maxNum, maxIndex = 0, 0

'''s1: O(n)
for i in range(len(myList)):
    if(myList[i] > max):
        max = myList[i]
        maxIndex = i
'''

'''s2: O(n) + O(n) 그러나 C 레벨 반복 + C 레벨 반복이기에 ㄱㅊ

maxNum = max(myList) 
maxIndex = myList.index(maxNum)
'''

#s3:  O(n)  enumerate 사용(값과 인덱스 한번에), 파이썬 레벨
for index, value in enumerate(myList):
    if(value > maxNum):
        maxNum = value
        maxIndex = index


print(maxNum, maxIndex+1)

