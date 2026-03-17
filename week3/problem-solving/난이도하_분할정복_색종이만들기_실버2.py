# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

import sys

n = int(sys.stdin.readline().strip())
matrix=[]
for _ in range(n):
    matrix.append( list(map(int, sys.stdin.readline().strip().split())))


white, blue = 0, 0

def isSameColor(row, col, size):
    color = matrix[row][col]
    for curRow in range(row, row+size):
        for curCol in range(col, col+size):
            if(matrix[curRow][curCol] != color):
                return False

    return True

def divide(startRow, startCol, sizeOfMatrix):
    '''
    베이스 케이스
    주어진 범위의 모든 칸을 순회하며 맨처음의 색과 같은지 
    다 같았다면 카운트
    다르면 조기 반환해서, 범위 나누기
    '''
    if(sizeOfMatrix == 0):
        return

    global white, blue
    if(isSameColor(startRow, startCol, sizeOfMatrix) == True):
        if(matrix[startRow][startCol] == 1):
            blue += 1
            return 
        else:
            white += 1
            return 

    #범위 나누기
    dividedSize = sizeOfMatrix // 2
    divide(startRow, startCol, dividedSize)
    divide(startRow+dividedSize, startCol, dividedSize)
    divide(startRow, startCol+dividedSize, dividedSize)
    divide(startRow+dividedSize, startCol+dividedSize, dividedSize)


divide(0, 0, n)

print(white)
print(blue)
