# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107
import sys

originInput = sys.stdin.readline().strip()

restored_ipv6=[]

#4자리로 채우는 함수
def fill_4(chunk):
    if len(chunk) != 4:
        return chunk.zfill(4)
    else:
        return chunk
    
#'::'가 있을 때
if '::' in originInput:
    left ,right = originInput.split('::')
    #print(f'left:{left}, right:{right}')

    leftList = list(left.split(':'))
    rightList= list(right.split(':'))
    #print(f'leftList:{leftList}, rightList:{rightList}')

    for chunk in leftList:
        restored_ipv6.append(fill_4(chunk))
    for _ in range(8-len(leftList)-len(rightList)):
        restored_ipv6.append('0'*4)
    for chunk in rightList:
        restored_ipv6.append(fill_4(chunk))

else:
    #print(originInput.split(':'))
    for chunk in originInput.split(':'):
        restored_ipv6.append(fill_4(chunk))
        
    #print(f'restored_ipv6: {restored_ipv6}')
                                                                                                                                                                    
print(':'.join(restored_ipv6))
