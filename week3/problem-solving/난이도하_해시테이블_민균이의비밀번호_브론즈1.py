# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
import sys

n = int(sys.stdin.readline().strip())
inputSet = set()
for _ in range(n):
    inputSet.add(sys.stdin.readline().strip())


def checkInverse(word):
    inversedWord=''
    for char in word[::-1]:
        inversedWord += char
    
    if(inversedWord in inputSet):
        return True
    
    return False


for word in inputSet:
    if(checkInverse(word) == True):
        size = len(word)
        print(f'{size} {word[size//2]}')
        break


