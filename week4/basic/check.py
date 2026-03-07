#!/usr/bin/env python3
"""
Week3 문제 채점 스크립트
"""

import subprocess
import sys
import difflib
import os

# Week3 문제 목록
PROBLEMS = {
    "01_binary_tree": "이진 트리 순회",
    "02_bst": "이진 검색 트리",
    "03_graph_basic": "그래프 기본",
    "04_bfs": "BFS",
    "05_dfs": "DFS",
    "06_topological_sort": "위상 정렬",
}

def check_problem(problem_name):
    """문제를 채점합니다."""
    problem_file = f"{problem_name}.py"
    output_file = f"{problem_name}_output.txt"
    
    if not os.path.exists(problem_file):
        print(f"❌ {problem_file} 파일이 없습니다.")
        return False
    
    if not os.path.exists(output_file):
        print(f"❌ {output_file} 파일이 없습니다.")
        return False
    
    # 문제 실행
    try:
        result = subprocess.run(
            ["python3", problem_file],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode != 0:
            print(f"❌ 실행 오류:")
            print(result.stderr)
            return False
        
        actual_output = result.stdout
        
    except subprocess.TimeoutExpired:
        print(f"❌ 시간 초과 (5초)")
        return False
    except Exception as e:
        print(f"❌ 실행 오류: {e}")
        return False
    
    # 예상 출력 읽기
    with open(output_file, 'r', encoding='utf-8') as f:
        expected_output = f.read()
    
    # 출력 비교
    if actual_output.strip() == expected_output.strip():
        print(f"✅ PASS")
        return True
    else:
        print(f"❌ FAIL")
        print("\n[예상 출력]")
        print(expected_output)
        print("\n[실제 출력]")
        print(actual_output)
        print("\n[차이점]")
        diff = difflib.unified_diff(
            expected_output.splitlines(keepends=True),
            actual_output.splitlines(keepends=True),
            fromfile='예상',
            tofile='실제'
        )
        print(''.join(diff))
        return False

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--all":
            # 모든 문제 채점
            print("=" * 50)
            print("Week3 전체 채점")
            print("=" * 50)
            
            passed = 0
            total = len(PROBLEMS)
            
            for problem_name, problem_title in PROBLEMS.items():
                print(f"\n[{problem_name}] {problem_title}")
                if check_problem(problem_name):
                    passed += 1
            
            print("\n" + "=" * 50)
            print(f"결과: {passed}/{total} 통과")
            print("=" * 50)
        else:
            # 특정 문제 채점 (번호만 입력)
            problem_num = sys.argv[1]
            if not problem_num.startswith("0"):
                problem_num = f"0{problem_num}"
            
            # 문제 찾기
            problem_name = None
            for name in PROBLEMS.keys():
                if name.startswith(problem_num):
                    problem_name = name
                    break
            
            if problem_name:
                print(f"[{problem_name}] {PROBLEMS[problem_name]}")
                check_problem(problem_name)
            else:
                print(f"❌ 문제 번호 {problem_num}를 찾을 수 없습니다.")
    else:
        print("사용법:")
        print("  python3 check.py --all           # 모든 문제 채점")
        print("  python3 check.py 1               # 1번 문제만 채점")
        print("  python3 check.py 01_binary_tree  # 특정 문제 채점")

if __name__ == "__main__":
    main()

