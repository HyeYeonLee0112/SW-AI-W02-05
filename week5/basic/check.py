#!/usr/bin/env python3
"""
Week4 문제 채점 스크립트
"""

import sys
import subprocess
import os
from pathlib import Path

# Week4 문제 목록
PROBLEMS = {
    "01_dp_fibonacci": "DP - 피보나치 (하향식)",
    "02_dp_stairs": "DP - 계단 오르기 (상향식)",
    "03_greedy_coin": "그리디 - 거스름돈",
    "04_greedy_meeting": "그리디 - 회의실 배정",
}

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
        print("사용법:")
        print("  python3 check.py --all           # 모든 문제 채점")
        print("  python3 check.py 1               # 1번 문제만 채점")
        print("  python3 check.py 01_dp_fibonacci # 특정 문제 채점")
        return
    
    # 모든 문제 채점
    if sys.argv[1] == '--all':
        print("=" * 60)
        print("Week4 전체 문제 채점")
        print("=" * 60)
        print()
        
        passed = 0
        failed = 0
        
        for problem_name, problem_title in PROBLEMS.items():
            problem_file = f"{problem_name}.py"
            print(f"📝 [{problem_name}] {problem_title}")
            success, message = check_solution(problem_file)
            
            if success:
                print(f"   {message}")
                passed += 1
            else:
                print(f"   ❌ FAIL")
                failed += 1
            print()
        
        print("=" * 60)
        print(f"결과: {passed}/{len(PROBLEMS)} 통과")
        print("=" * 60)
        
    else:
        # 특정 문제 채점 (번호만 입력 또는 파일명 입력)
        input_arg = sys.argv[1]
        
        # 번호만 입력한 경우 (예: 1, 01)
        if input_arg.isdigit() or (input_arg.startswith('0') and len(input_arg) == 2):
            problem_num = input_arg
            if not problem_num.startswith("0"):
                problem_num = f"0{problem_num}"
            
            # 문제 찾기
            problem_name = None
            for name in PROBLEMS.keys():
                if name.startswith(problem_num):
                    problem_name = name
                    break
            
            if problem_name:
                problem_file = f"{problem_name}.py"
                print("=" * 60)
                print(f"[{problem_name}] {PROBLEMS[problem_name]}")
                print("=" * 60)
                print()
            else:
                print(f"❌ 문제 번호 {problem_num}를 찾을 수 없습니다.")
                print("\n사용법:")
                print("  python3 check.py --all    # 모든 문제 채점")
                print("  python3 check.py 1        # 1번 문제만 채점")
                print("  python3 check.py 01_dp_fibonacci  # 특정 문제 채점")
                return
        else:
            # 파일명 입력한 경우
            problem_file = input_arg
            if not problem_file.endswith('.py'):
                problem_file += '.py'
            
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

