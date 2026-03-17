# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
import sys

class Node:
    def __init__(self, data=0, lp=None, rp=None):
        self.data = data
        self.lp = lp
        self.rp = rp

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None
        #커서가 ***오른쪽***을 가리킨다고 가정
    
    def insert(self, data):
        #커서가 가르키는 노드의 왼쪽에 삽입한다
        new_node = Node(data)

        # '|'인 경우
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
            self.cursor = None
            return
        
        #'abc|': 커서가 꼬리 오른쪽인 경우
        elif(self.cursor == None):
            last_node = self.tail

            last_node.rp = new_node
            new_node.lp = last_node

            self.tail = new_node
            return

        #'|abc'커서의 왼쪽이 헤드인 경우
        elif(self.cursor.lp == None):
            self.head = new_node

            new_node.rp = self.cursor
            self.cursor.lp = new_node
            return

        #'ab|c':노드 사이에 넣는 일반적인  경우
        else:
            right_node = self.cursor
            left_node = right_node.lp

            #왼쪽 연결
            left_node.rp = new_node
            new_node.lp = left_node

            #오른쪽 연결
            right_node.lp = new_node
            new_node.rp = right_node
            return

    def left(self):

        #커서가 맨 앞인 경우: 무시
        if(self.cursor == self.head):
            return

        #커서가 맨 뒤에 있는 경우
        elif(self.cursor == None):
            self.cursor = self.tail
            return

        #커서가 노드 사이에 있는 일반적인 경우
        else: 
            self.cursor = self.cursor.lp
            return
       
    def right(self):

        #커서가 맨 뒤인 경우 무시
        if(self.cursor == None):
            return
    
        #커서가 중간에 있는 일반적인 경우
        else:
            self.cursor = self.cursor.rp
    
    def delete(self):
        #커서의 가르키는 노드의 왼쪽에 있는 문자 삭제

        #1. '|'/'|abc': 커서의 왼쪽에 지울 게 없는 경우
        if(self.head == None  or self.cursor == self.head):
            return
        
        #2. 'a|': 노드가 하나인데 삭제하는 경우
        elif(self.cursor == None and self.head == self.tail):
            self.head = None
            self.tail = None
            self.cursor = None

        #3. 'abc|': 맨 뒤 노드 삭제하는 경우
        elif(self.cursor == None):

            delete_node = self.tail
            last_node = delete_node.lp

            last_node.rp = None
            delete_node.lp = None

            self.tail = last_node

        #4. 'a|bs' 맨 앞 노드 지우는 경우
        elif(self.cursor.lp == self.head):
            right_node = self.cursor
            delete_node = right_node.lp

            delete_node.rp = None
            right_node.lp = None
            self.head = right_node

        #5. 'ab|c': 커서가 노드 중간에 있는 일반적인 경우
        else:
            #노드
            delete_node = self.cursor.lp
            left_node = delete_node.lp
            right_node = self.cursor
            
            #왼쪽 참조 끊기
            left_node.rp = right_node
            delete_node.lp = None

            #오른쪽 참조 끊기
            right_node.lp = left_node
            delete_node.rp = None


    def print(self):
        result=''
        
        cur_p = self.head
        while(cur_p != None):
            result += cur_p.data
            cur_p = cur_p.rp
        
        print(result)
        

def instruct(linkedList, commandLine):

    command = commandLine[0]

    if(command == "L"):
        linkedList.left()
    elif(command == "D"):
        linkedList.right()
    elif(command == "B"):
        linkedList.delete()
    elif(command == "P"):
        data = commandLine[1]
        linkedList.insert(data)

#입력
originString = sys.stdin.readline().strip()
m = int(sys.stdin.readline())

#명령어 입력
commands = []
for _ in range(m):
    command = sys.stdin.readline().split()
    commands.append(command)

#링크드 리스트 생성
ll = LinkedList()
for char in originString:
    ll.insert(char)

#명령어 처리
for c in commands:
    instruct(ll, c)

ll.print()
