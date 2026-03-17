# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

# 수학적 모듈러 연산을 이용..=> 한 번 증명 해보고 걍 외워라
#(x * x) % c = ((x % c) * (x % c)) % c
#(x * y) % c = ((x % c) * (y % c)) % c

import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

def mod_pow(base, exp, mod):

    #베이스 케이스: 지수가 1인 경우의 나머지 
    if(exp == 1):
        return (base % mod)

    #지수가 짝수인 경우
    if(exp%2 == 0):
        
        midExp = exp // 2
        half = mod_pow(base, midExp, mod)
        return (half*half) % mod

    #지수가 홀수인 경우
    else:
        midExp = exp // 2
        half = mod_pow(base, midExp, mod)
        return (half*half*base) % mod
        
result = mod_pow(arr[0], arr[1], arr[2])
print(result)