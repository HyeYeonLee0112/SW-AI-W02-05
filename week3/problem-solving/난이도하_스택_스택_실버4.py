# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

import sys

myStack=[]
result = []

def push(num):
    return myStack.append(num)

def size():
    return len(myStack)

def top():
    if(size() == 0):
        return -1

    return myStack[-1]

def pop():

    if(size() == 0):
        return -1

    topOfStack = top()
    myStack.pop()
    return topOfStack

def empty():
    if(size() == 0):
        return 1
    else:
        return 0

def instruct(input):
    command = input[0]

    if command == "push":
        push(input[1])
    elif command == "top":
        result.append(top())
    elif command == "size":
        result.append(size())
    elif command == "empty":
        result.append(empty())
    elif command == "pop":
        result.append(pop())

n = int(sys.stdin.readline())

for _ in range(n):
    instruct(sys.stdin.readline().split())

for r in result:
    print(r)