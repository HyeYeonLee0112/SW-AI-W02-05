# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
'''
m-1개: 중심이 될 노드에 하나 잡고 m-1개를 연결
1개: 남은 노드 전부 일직선으로 연결시키기

중심노드는 예제 출력을 쭉 보면 1이다...
예제 입력과 문제 분석 뿐만 아닌, 예제 출력까지도 보고 로직을 짜야 한다
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = [] #결과 저장

center = 1 #중심 노드
#중심노드와 연결될 m-1개의 노드
leaves1 = [ i for i in range(m)
    if i != center #중심 노드 제외
]

#leavs1에 대한 리프 만들기
for leaf in leaves1:

    #중심노드와 leaf연결
    leaf1 = min(center, leaf)
    leaf2 = max(center, leaf)
    result.append([leaf1, leaf2])


#나머지 일직선 리프 만들기
if(leaves1[-1] != (n-1) ):

    u = center
    startLeaf = len(leaves1)+1
    for leaf in range(startLeaf, n):
        v = leaf
        result.append([u, v])
        u = v

#출력
for r in result:
    print(r[0], r[1])