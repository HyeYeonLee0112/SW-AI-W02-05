# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

import sys

#입력
c = int(sys.stdin.readline())
scoreList = []
for _ in range(c):
    case = list(map(int, sys.stdin.readline().split()))
    scoreList.append(case)

#결과 리스트
result = []

for group in range(c):
    #평균 계산
    sumScore = 0
    numsOfStudent = scoreList[group][0]
    for student in range(1,numsOfStudent+1):
        sumScore += scoreList[group][student]
    avg = sumScore / numsOfStudent
    #print(f"평균은 {avg}")

    #비율 계산
    numsOfAboveAvg = 0
    for student in range(1, numsOfStudent+1):
        if(scoreList[group][student] > avg):
            numsOfAboveAvg += 1

    percentage = round( (numsOfAboveAvg/numsOfStudent) * 100 , 3)
    result.append(percentage)

for percentage in result:    
    print(f"{percentage:.3f}%")