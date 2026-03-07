#!/usr/bin/env python3
"""
GitHub Issues 일괄 삭제/닫기 스크립트

사용법:
    python clear_issues.py --close      # 모든 이슈 닫기
    python clear_issues.py --delete     # 모든 이슈 삭제 (복구 불가)
    python clear_issues.py --dry-run    # 실제로 실행하지 않고 미리보기
"""

import requests
import sys

# secrets.py에서 설정 불러오기
from secrets import GITHUB_TOKEN, REPO_OWNER, REPO_NAME


def get_all_issues(repo_owner, repo_name, token):
    """모든 이슈 가져오기 (open + closed)"""
    issues = []
    page = 1
    per_page = 100
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    while True:
        url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
        params = {
            'state': 'all',
            'per_page': per_page,
            'page': page,
            'filter': 'all'
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"❌ 이슈 목록을 가져오는데 실패했습니다: {response.status_code}")
            print(f"   {response.text}")
            break
        
        page_issues = response.json()
        
        if not page_issues:
            break
        
        # Pull Request 제외 (이슈만 필터링)
        for issue in page_issues:
            if 'pull_request' not in issue:
                issues.append(issue)
        
        page += 1
    
    return issues


def close_issue(repo_owner, repo_name, token, issue_number):
    """이슈 닫기"""
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}'
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    data = {'state': 'closed'}
    
    response = requests.patch(url, headers=headers, json=data)
    return response.status_code == 200


def delete_issue(token, issue_node_id):
    """이슈 삭제 (GraphQL API 사용)"""
    url = 'https://api.github.com/graphql'
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    query = '''
    mutation($issueId: ID!) {
        deleteIssue(input: {issueId: $issueId}) {
            clientMutationId
        }
    }
    '''
    
    data = {
        'query': query,
        'variables': {'issueId': issue_node_id}
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        if 'errors' in result:
            return False, result['errors'][0]['message']
        return True, None
    return False, response.text


def main():
    # 커맨드 라인 인자 확인
    if len(sys.argv) < 2:
        print("사용법: python clear_issues.py [--close | --delete] [--dry-run]")
        print("")
        print("옵션:")
        print("  --close    모든 이슈를 닫기 (복구 가능)")
        print("  --delete   모든 이슈를 삭제 (복구 불가)")
        print("  --dry-run  실제로 실행하지 않고 미리보기")
        print("")
        print("예시:")
        print("  python clear_issues.py --close --dry-run")
        print("  python clear_issues.py --delete")
        sys.exit(1)
    
    dry_run = '--dry-run' in sys.argv
    close_mode = '--close' in sys.argv
    delete_mode = '--delete' in sys.argv
    
    if not close_mode and not delete_mode:
        print("❌ --close 또는 --delete 옵션을 지정해주세요.")
        sys.exit(1)
    
    if close_mode and delete_mode:
        print("❌ --close와 --delete 옵션은 동시에 사용할 수 없습니다.")
        sys.exit(1)
    
    # 설정 확인
    if not dry_run:
        if GITHUB_TOKEN == "your_token_here" or REPO_OWNER == "your_github_username_or_org":
            print("❌ secrets.py 파일의 설정을 먼저 입력해주세요.")
            sys.exit(1)
    
    mode_text = "삭제" if delete_mode else "닫기"
    print(f"🗑️  이슈 일괄 {mode_text}")
    print(f"🎯 대상 레포: {REPO_OWNER}/{REPO_NAME}")
    
    if dry_run:
        print("\n🔍 DRY RUN 모드 (실제로 실행하지 않음)\n")
    elif delete_mode:
        print("\n⚠️  경고: 삭제된 이슈는 복구할 수 없습니다!")
        confirm = input("정말 모든 이슈를 삭제하시겠습니까? (yes/no): ")
        if confirm.lower() != 'yes':
            print("취소되었습니다.")
            sys.exit(0)
        print("")
    else:
        print("")
    
    # 이슈 목록 가져오기
    print("🔍 이슈 목록을 가져오는 중...")
    issues = get_all_issues(REPO_OWNER, REPO_NAME, GITHUB_TOKEN)
    
    if not issues:
        print("📭 삭제/닫을 이슈가 없습니다.")
        sys.exit(0)
    
    print(f"📊 총 {len(issues)}개 이슈 발견\n")
    
    # 이슈 처리
    success_count = 0
    fail_count = 0
    
    for idx, issue in enumerate(issues, 1):
        issue_number = issue['number']
        issue_title = issue['title']
        issue_state = issue['state']
        
        if dry_run:
            print(f"[{idx:3d}/{len(issues)}] #{issue_number} ({issue_state}) {issue_title}")
            success_count += 1
        elif close_mode:
            if issue_state == 'closed':
                print(f"⏭️  [{idx:3d}/{len(issues)}] #{issue_number} (이미 닫힘) {issue_title}")
                success_count += 1
            else:
                if close_issue(REPO_OWNER, REPO_NAME, GITHUB_TOKEN, issue_number):
                    print(f"✅ [{idx:3d}/{len(issues)}] #{issue_number} {issue_title}")
                    success_count += 1
                else:
                    print(f"❌ [{idx:3d}/{len(issues)}] #{issue_number} {issue_title}")
                    fail_count += 1
        elif delete_mode:
            node_id = issue['node_id']
            success, error = delete_issue(GITHUB_TOKEN, node_id)
            if success:
                print(f"✅ [{idx:3d}/{len(issues)}] #{issue_number} {issue_title}")
                success_count += 1
            else:
                print(f"❌ [{idx:3d}/{len(issues)}] #{issue_number} {issue_title}")
                if error:
                    print(f"   Error: {error}")
                fail_count += 1
    
    # 결과 요약
    print("\n" + "="*70)
    print(f"✨ 완료!")
    print(f"   성공: {success_count}개")
    if fail_count > 0:
        print(f"   실패: {fail_count}개")
    print("="*70)
    
    if dry_run:
        print(f"\n💡 실제로 실행하려면 --dry-run 옵션을 제거하세요:")
        if close_mode:
            print("   python clear_issues.py --close")
        else:
            print("   python clear_issues.py --delete")


if __name__ == "__main__":
    main()
