# 📋 GitHub Issues 일괄 생성 및 GitHub Projects 일괄 등록 가이드

## 🛠️ 환경 설정 (venv)

Python 가상환경을 사용하여 의존성을 관리합니다.

### 1. 가상환경 생성

```bash
# 가상환경 생성
python -m venv .venv
```

### 2. 가상환경 활성화

```bash
# macOS / Linux
source .venv/bin/activate

# Windows (CMD)
.venv\Scripts\activate.bat

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 3. 가상환경 비활성화

```bash
deactivate
```

> 💡 **팁**: 가상환경이 활성화되면 터미널 프롬프트 앞에 `(.venv)`가 표시됩니다.

---

## 📁 파일 구성

```
ISSUE_TEMPLATE/
├── csv_to_issues.py              # Issue 생성 스크립트
├── clear_issues.py               # Issue 삭제/닫기 스크립트
├── secrets.py.example            # 설정 파일 샘플
├── requirements.txt              # Python 패키지
├── week2_issues_complete.csv     # Week 2 문제 목록
├── week3_issues_complete.csv     # Week 3 문제 목록
├── week4_issues_complete.csv     # Week 4 문제 목록
├── week5_issues_complete.csv     # Week 5 문제 목록
├── week6_issues_complete.csv     # Week 6 문제 목록
├── week7_issues_complete.csv     # Week 7 문제 목록
├── week8_issues_complete.csv     # Week 8 문제 목록
├── week9_issues_complete.csv     # Week 9 문제 목록
├── week10_issues_complete.csv    # Week 10 문제 목록
├── week11-12_issues_complete.csv # Week 11-12 문제 목록
├── week13-14_issues_complete.csv # Week 13-14 문제 목록
└── README.md                     # 이 문서
```

## 🚀 빠른 시작

### 1️⃣ 패키지 설치

```bash
pip install -r requirements.txt
```

### 2️⃣ 설정 파일 생성

`secrets.py.example` 파일을 복사하여 `secrets.py`를 생성하고 설정을 입력합니다:

```bash
# 설정 파일 복사
cp secrets.py.example secrets.py

## 🔑 GitHub Token 생성

1. GitHub 설정으로 이동: https://github.com/settings/tokens
2. **"Tokens (classic)"** 선택
3. **"Generate new token"** > **"Generate new token (classic)"** 클릭
4. 권한 설정:
   - `repo` (전체) - 필수

# secrets.py 파일을 열어서 아래 정보 입력
# - GITHUB_TOKEN: GitHub Personal Access Token
# - REPO_OWNER: 레포지토리 소유자 (예: rayee)
# - REPO_NAME: 레포지토리 이름 (예: SW-AI-PINTOS)
```

> 📌 **REPO_NAME 설명**
> - 해당 주차에 실제로 사용하는 본인의 **PUBLIC** 레포여야 합니다.
> - 팀 단위 과제의 경우 해당 팀 레포지토리를 기준으로 합니다.
> - 알고리즘, 핀토스 등 레포지토리 1개로 복수의 주차를 사용할 경우 전주에 사용한 레포를 그대로 이용가능합니다.

## 📁 예시 

```
📂 SW-AI-Algorithm (레포지토리 1개)
├── 📋 Issues
│   ├── [WEEK2] basic - 파이썬 문법 - ...
│   ├── [WEEK2] 배열 - 평균은 넘겠지
│   ├── [WEEK3] basic - 이분탐색 - ...
│   ├── [WEEK3] 스택 - 스택
│   ├── [WEEK4] ...
│   └── [WEEK5] ...
│
└── 📊 Projects (4개)
    ├── Week 2 Project → [WEEK2] 이슈만 추가
    ├── Week 3 Project → [WEEK3] 이슈만 추가
    ├── Week 4 Project → [WEEK4] 이슈만 추가
    └── Week 5 Project → [WEEK5] 이슈만 추가
```

⚠️ **중요**: `secrets.py`는 `.gitignore`에 포함되어 있어 Git에 커밋되지 않습니다.


### 3️⃣ Issues 생성

```bash
# Dry-run (실제로 생성하지 않고 미리보기)
python csv_to_issues.py week2_issues_complete.csv --dry-run

# 실제 생성 
python csv_to_issues.py week2_issues_complete.csv
```

### 4️⃣ Issues 삭제/닫기

잘못등록한 경우 기존 이슈를 일괄 삭제하거나 닫을 수 있습니다.

```bash
# Dry-run (미리보기)
python clear_issues.py --close --dry-run
python clear_issues.py --delete --dry-run

# 모든 이슈 닫기 (복구 가능)
python clear_issues.py --close

# 모든 이슈 삭제 (복구 불가 ⚠️)
python clear_issues.py --delete
```

| 옵션 | 설명 |
|------|------|
| `--close` | 모든 이슈를 닫기 (나중에 다시 열 수 있음) |
| `--delete` | 모든 이슈를 완전히 삭제 (복구 불가) |
| `--dry-run` | 실제로 실행하지 않고 미리보기 |

> ⚠️ **주의**: `--delete` 옵션은 이슈를 완전히 삭제하므로 복구할 수 없습니다. 신중하게 사용하세요.

## 🔄 GitHub Projects에 추가하기

Issues를 생성한 후, GitHub Projects에 추가하는 방법:

### 1. GitHub Project 생성 (사용중인 GitHub Project가 있다면, 그대로 유용해도 됨.)

1. Repository의 **Projects** 탭으로 이동
2. **"New project"** 클릭
3. **"Board"** 템플릿 선택
4. 프로젝트 이름 입력 

### 2. Issues를 Project에 추가

1. Project 보드 열기
2. **"+"** 클릭 후 **"Add items to project"**
3. 해당 WEEK 검색 (예: WEEk5)

### 3. 보드 구성

**Status 컬럼:**
- 📋 **Todo** - 아직 시작 안 함
- 🔄 **In Progress** - 진행 중
- ✅ **Done** - 완료

