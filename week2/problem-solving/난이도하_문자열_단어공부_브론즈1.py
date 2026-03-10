# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
import sys

word = sys.stdin.readline().strip().lower()

seenDict = {}

#가장 많은 문자 
for key in word:
    if key not in seenDict:
        seenDict[key] = 1
    else:
        seenDict[key] += 1

maxCount = max(seenDict.values())
numsOfDuplicate = 0
result = ""

for key, value in seenDict.items():
    if(value == maxCount):
        numsOfDuplicate += 1
        result = key
    

#출력
if numsOfDuplicate > 1:
    print("?")
else:
    print(result.upper())