# 시간 복잡도: n번 반복되므로, O(n)

import sys
input = sys.stdin.readline

n = int(input()) # 명령의 수 n개
stack = []
index = -1

for i in range(n):
    use_input = input().split()
    command = use_input[0]
    if len(use_input) >= 2:
        x = int(use_input[1])

    match command:
        case '1':
            stack.append(x) # 리스트에 요소 추가하는 것: O(1)
            index += 1
        case '2':
            if index >= 0:
                print(stack.pop()) # 리스트에 요소 꺼내는 것: O(1)
                index -= 1
            else: print(-1)
        case '3':
            print(len(stack))
        case '4':
            if index == -1: print(1)
            else: print(0)
        case '5':
            if index >= 0:
                print(stack[-1]) # 리스트의 특정 인덱스 접근 O(1)
            else: print(-1)