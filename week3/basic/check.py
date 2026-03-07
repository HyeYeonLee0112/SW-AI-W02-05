#!/usr/bin/env python3
"""
알고리즘 학습 문제 채점 스크립트

사용법:
  python check.py <문제파일명>
  예: python check.py python_basic.py

또는 모든 문제 채점:
  python check.py --all
"""

import sys
import subprocess
import os
from pathlib import Path

def check_solution(problem_file):
    """
    문제 파일을 실행하고 정답과 비교
    
    Args:
        problem_file: 문제 파일 경로
    
    Returns:
        (passed, message) 튜플
    """
    # 파일 존재 확인
    if not os.path.exists(problem_file):
        return False, f"❌ 파일을 찾을 수 없습니다: {problem_file}"
    
    # output 파일 경로
    base_name = problem_file.replace('.py', '')
    output_file = f"{base_name}_output.txt"
    
    if not os.path.exists(output_file):
        return False, f"❌ 정답 파일을 찾을 수 없습니다: {output_file}"
    
    try:
        # 문제 파일 실행
        result = subprocess.run(
            ['python3', problem_file],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode != 0:
            return False, f"❌ 실행 오류:\n{result.stderr}"
        
        # 실제 출력
        actual_output = result.stdout.strip()
        
        # 정답 출력 읽기
        with open(output_file, 'r', encoding='utf-8') as f:
            expected_output = f.read().strip()
        
        # 비교 (공백 정규화)
        actual_lines = [line.strip() for line in actual_output.split('\n') if line.strip()]
        expected_lines = [line.strip() for line in expected_output.split('\n') if line.strip()]
        
        if actual_lines == expected_lines:
            return True, "✅ PASS - 정답입니다!"
        else:
            # 차이점 찾기
            diff_msg = "❌ FAIL - 출력이 다릅니다.\n\n"
            diff_msg += "=== 예상 출력 ===\n"
            diff_msg += expected_output[:500]  # 처음 500자만
            if len(expected_output) > 500:
                diff_msg += "\n... (생략)"
            diff_msg += "\n\n=== 실제 출력 ===\n"
            diff_msg += actual_output[:500]
            if len(actual_output) > 500:
                diff_msg += "\n... (생략)"
            
            return False, diff_msg
            
    except subprocess.TimeoutExpired:
        return False, "❌ 시간 초과 (10초)"
    except Exception as e:
        return False, f"❌ 오류 발생: {str(e)}"

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    # 모든 문제 채점
    if sys.argv[1] == '--all':
        print("=" * 60)
        print("Week2 전체 문제 채점")
        print("=" * 60)
        print()
        
        problem_files = [
            '01_binary_search.py',
            '02_divide_conquer.py',
            '03_quick_sort.py',
            '04_merge_sort.py',
            '05_stack.py',
            '06_queue.py',
            '07_priority_queue.py',
            '08_linked_list.py',
            '09_hash_table.py'
        ]
        
        passed = 0
        failed = 0
        
        for problem_file in problem_files:
            print(f"📝 {problem_file}")
            success, message = check_solution(problem_file)
            
            if success:
                print(f"   {message}")
                passed += 1
            else:
                print(f"   ❌ FAIL")
                failed += 1
            print()
        
        print("=" * 60)
        print(f"결과: {passed}개 통과, {failed}개 실패 (총 {passed + failed}개)")
        print("=" * 60)
        
    else:
        # 단일 문제 채점
        problem_file = sys.argv[1]
        
        print("=" * 60)
        print(f"문제: {problem_file}")
        print("=" * 60)
        print()
        
        success, message = check_solution(problem_file)
        print(message)
        print()
        
        if success:
            print("🎉 축하합니다! 문제를 해결했습니다!")
        else:
            print("💡 힌트: 문제 파일의 TODO 부분을 다시 확인해보세요.")

if __name__ == '__main__':
    main()

