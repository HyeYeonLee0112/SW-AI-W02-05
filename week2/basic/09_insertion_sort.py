"""
[삽입 정렬 구현]

문제 설명:
- 삽입 정렬(Insertion Sort) 알고리즘을 구현합니다.
- 정렬된 부분에 새로운 원소를 적절한 위치에 삽입하는 방식입니다.
- 카드 게임에서 손에 든 카드를 정렬하는 방식과 유사합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [12, 11, 13, 5, 6]
출력: [5, 6, 11, 12, 13]

힌트:
- 첫 번째 원소는 이미 정렬되어 있다고 가정
- 두 번째 원소부터 시작하여 앞의 정렬된 부분에 삽입
- 삽입 위치를 찾기 위해 뒤에서 앞으로 비교
"""

def insertion_sort(arr):
    """
    삽입 정렬 구현
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    n = len(arr)
    
    # TODO: 두 번째 원소(인덱스 1)부터 시작
    ## 각 원소를 정렬된 부분에 삽입
    ## 현재 원소를 key에 저장    
    ## key를 삽입할 위치 찾기
    ## j는 key 바로 앞 인덱스부터 시작
    ## arr[j] > key인 동안 원소를 오른쪽으로 이동
    ## 찾은 위치에 key 삽입
    pass
    
    return arr

def insertion_sort_with_steps(arr):
    """
    과정을 출력하는 삽입 정렬
    """
    n = len(arr)
    print(f"초기 배열: {arr}")
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        print(f"\nStep {i}: key = {key}")
        print(f"정렬된 부분: {arr[:i]}")
        
        # TODO: 삽입 위치 찾기 및 이동
        pass
        
        arr[j + 1] = key
        print(f"삽입 후: {arr}")
    
    return arr

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [12, 11, 13, 5, 6]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = insertion_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2: 과정 출력
    arr2 = [5, 2, 4, 6, 1, 3]
    print("=== 테스트 케이스 2: 정렬 과정 ===")
    result2 = insertion_sort_with_steps(arr2.copy())
    print()
    
    # 테스트 케이스 3: 이미 정렬된 배열
    arr3 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 3: 이미 정렬됨 ===")
    print(f"정렬 전: {arr3}")
    result3 = insertion_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print("이미 정렬된 경우 O(n) 시간 소요")


