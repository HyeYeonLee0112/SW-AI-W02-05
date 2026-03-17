# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

import sys
input = sys.stdin.readline
'''
def BN(i, j):
    next_s = next[i]

    next[i] = j
    next[j] = next_s
    
    prev[j] = i
    prev[next_s] = j

    return next_s

def BP(i, j):
    prev_s = prev[i]

    next[prev_s] = j
    next[j] = i

    prev[i] = j
    prev[j] = prev_s

    return prev_s

def CN(i):
    closing_s = next[i]
    next_s = next[closing_s]

    next[i] = next_s
    prev[next_s] = i

    return closing_s

def CP(i):
    closing_s = prev[i]
    prev_s = prev[closing_s]

    next[prev_s] = i
    prev[i] = prev_s
    
    return closing_s

'''


#입력
n, m = map(int, input().split())
stations = list(map(int, input().split()))

#전역, 다음역에 대한 배열 정리
MAX = 1000001
prev = [0 for _ in range(MAX)]
nxt = [0 for _ in range(MAX)]

for index in range(n):
    
    cur_station = stations[index]
    next_station = stations[(index+1) % n]

    nxt[cur_station] = next_station
    prev[next_station] = cur_station

#명령어 처리
result=[]
for _ in range(m):
    cmd_line = sys.stdin.readline().split()

    command=cmd_line[0]
    i = int(cmd_line[1])

    r = 0
    if(command == "BN"):
        j = int(cmd_line[2])
        next_s = nxt[i]

        nxt[i] = j
        nxt[j] = next_s
        
        prev[j] = i
        prev[next_s] = j

        r = next_s
    elif(command == "BP"):
        j = int(cmd_line[2])
        prev_s = prev[i]

        nxt[prev_s] = j
        nxt[j] = i

        prev[i] = j
        prev[j] = prev_s

        r = prev_s
    elif(command == "CN"):
        closing_s = nxt[i]
        next_s = nxt[closing_s]

        nxt[i] = next_s
        prev[next_s] = i

        r = closing_s
    elif(command == "CP"):
        closing_s = prev[i]
        prev_s = prev[closing_s]

        nxt[prev_s] = i
        prev[i] = prev_s
        
        r = closing_s

    result.append(str(r))

sys.stdout.write('\n'.join(result))