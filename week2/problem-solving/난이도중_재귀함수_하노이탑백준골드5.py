# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914
import sys

k = int(sys.stdin.readline().strip())
result = []

def hanoiTower(numsOfPlates, start, assist, end):

    #원판이 한개 남은 경우
    if(numsOfPlates==1):
        #result.append(f'{start} {end}')
        print(f'{start} {end}')
        return
    
    #start에 있는 n-1개의 기둥들을 보조기둥(assist) 옮기기
    #잠시 목표 기둥을 보조 기둥 취급
    hanoiTower(numsOfPlates-1, start, end, assist)
    print(f'{start} {end}')
    #result.append(f'{start} {end}')

    #start에 있는 마지막 제일 큰 기둥을 목표 기둥으로 옮기기
    #result.append(f'{start} {end}')

    #보조 기둥에 있던 n-1개의 기둥들을 목표 기둥에 옮기기
    hanoiTower(numsOfPlates-1, assist, start, end)

def hanoi_count(n):
    if n == 1:
        return 1
    return 2 * hanoi_count(n - 1) + 1

count = hanoi_count(k)
print(count)

if(k <= 20):
    hanoiTower(k, 1, 2, 3)

    # for c in range(count):
    #     print(result[c])
