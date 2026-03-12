# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

import sys

#입력
n = int(sys.stdin.readline())
#퀸의 위치 저장: 인덱스는 행, 값은 열
queenPos = [0, ] #1베이스??
count= 0

def nQueen(col):
    #베이스 케이스: 퀸 포스가 4자리인지
    if(col == n+1):
        count += 1
        return
    
    #각 행을 따라가며 넣을 수 있는 열 찾기
    for row in range(1,n+1):
        
        #
        if(len(queenPos) != row):
            #1. 선택
            queenPos.append(row)

            #2. 탐색
            


            #3. 취소

        
        pass

    pass