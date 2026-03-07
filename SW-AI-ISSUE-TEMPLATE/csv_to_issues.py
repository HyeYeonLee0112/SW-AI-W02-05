#!/usr/bin/env python3
"""
GitHub Issues 일괄 생성 스크립트

사용법:
    python csv_to_issues.py week2_issues_complete.csv
    python csv_to_issues.py week2_issues_complete.csv --dry-run
"""

import csv
import json
import requests
import sys
import re
from pathlib import Path

# secrets.py에서 설정 불러오기
from secrets import GITHUB_TOKEN, REPO_OWNER, REPO_NAME


def extract_week_number(filename):
    """파일명에서 week 번호 추출 (예: week2_issues_complete.csv -> 2, week11-12_issues_complete.csv -> 11-12)"""
    # 먼저 범위 형식 (11-12, 13-14) 체크
    match = re.search(r'week(\d+-\d+)', filename)
    if match:
        return match.group(1)
    # 단일 숫자 형식 체크
    match = re.search(r'week(\d+)', filename)
    if match:
        return match.group(1)
    return None


def get_existing_issues(repo_owner, repo_name, token):
    """기존 이슈 제목 목록 가져오기 (중복 방지용)"""
    existing_titles = set()
    page = 1
    per_page = 100
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    while True:
        url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
        params = {
            'state': 'all',  # open + closed 모두 가져오기
            'per_page': per_page,
            'page': page
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"⚠️  기존 이슈 목록을 가져오는데 실패했습니다: {response.status_code}")
            break
        
        issues = response.json()
        
        if not issues:
            break
        
        for issue in issues:
            existing_titles.add(issue['title'])
        
        page += 1
    
    return existing_titles


def create_github_issue(repo_owner, repo_name, token, title, content, week_num):
    """GitHub Issue 생성"""
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # 이슈 제목: [WEEK{숫자}] 제목
    issue_title = f"[WEEK{week_num}] {title}"
    
    # 이슈 본문: content가 있으면 URL만 표시, 없으면 빈 문자열
    issue_body = content.strip() if content.strip() else ""
    
    data = {
        'title': issue_title,
        'body': issue_body
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    return response


def main():
    # 커맨드 라인 인자 확인
    if len(sys.argv) < 2:
        print("사용법: python csv_to_issues.py <csv_file> [--dry-run]")
        print("예시: python csv_to_issues.py week2_issues_complete.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    
    # 파일 존재 확인
    if not Path(csv_file).exists():
        print(f"❌ 파일을 찾을 수 없습니다: {csv_file}")
        sys.exit(1)
    
    # Week 번호 추출
    week_num = extract_week_number(csv_file)
    if not week_num:
        print(f"⚠️  파일명에서 week 번호를 찾을 수 없습니다: {csv_file}")
        print("기본값 '2'를 사용합니다.")
        week_num = '2'
    
    # 설정 확인
    if not dry_run:
        if GITHUB_TOKEN == "your_token_here" or REPO_OWNER == "your_github_username_or_org":
            print("❌ secrets.py 파일의 설정을 먼저 입력해주세요:")
            print("   - GITHUB_TOKEN")
            print("   - REPO_OWNER")
            print("   - REPO_NAME")
            sys.exit(1)
    
    # CSV 파일 읽기
    problems = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['title'] and row['title'].strip():  # 빈 줄 무시
                problems.append({
                    'title': row['title'].strip(),
                    'content': (row.get('content') or '').strip()
                })
    
    print(f"📋 Week {week_num} 이슈 생성")
    print(f"📂 파일: {csv_file}")
    print(f"📊 총 {len(problems)}개 문제")
    
    # 기존 이슈 목록 가져오기 (중복 방지)
    existing_titles = set()
    if not dry_run:
        print(f"🎯 대상 레포: {REPO_OWNER}/{REPO_NAME}")
        print("🔍 기존 이슈 목록 확인 중...")
        existing_titles = get_existing_issues(REPO_OWNER, REPO_NAME, GITHUB_TOKEN)
        print(f"📌 기존 이슈: {len(existing_titles)}개\n")
    else:
        print("\n🔍 DRY RUN 모드 (실제로 생성하지 않음)\n")
    
    # 이슈 생성
    success_count = 0
    fail_count = 0
    skip_count = 0
    
    for idx, problem in enumerate(problems, 1):
        issue_title = f"[WEEK{week_num}] {problem['title']}"
        
        if dry_run:
            print(f"[{idx:2d}/{len(problems)}] {issue_title}")
            if problem['content']:
                print(f"         └─ 링크: {problem['content']}")
            success_count += 1
        else:
            # 중복 체크: 이미 존재하는 이슈면 건너뛰기
            if issue_title in existing_titles:
                print(f"⏭️  [{idx:2d}/{len(problems)}] {issue_title} (이미 존재)")
                skip_count += 1
                continue
            
            response = create_github_issue(
                REPO_OWNER,
                REPO_NAME,
                GITHUB_TOKEN,
                problem['title'],
                problem['content'],
                week_num
            )
            
            if response.status_code == 201:
                print(f"✅ [{idx:2d}/{len(problems)}] {issue_title}")
                success_count += 1
            else:
                print(f"❌ [{idx:2d}/{len(problems)}] {issue_title}")
                print(f"   Error: {response.status_code} - {response.text}")
                fail_count += 1
    
    # 결과 요약
    print("\n" + "="*70)
    print(f"✨ 완료!")
    print(f"   성공: {success_count}개")
    if skip_count > 0:
        print(f"   건너뜀 (중복): {skip_count}개")
    if fail_count > 0:
        print(f"   실패: {fail_count}개")
    print("="*70)
    
    if dry_run:
        print("\n💡 실제로 생성하려면 --dry-run 옵션을 제거하세요:")
        print(f"   python csv_to_issues.py {csv_file}")


if __name__ == "__main__":
    main()
