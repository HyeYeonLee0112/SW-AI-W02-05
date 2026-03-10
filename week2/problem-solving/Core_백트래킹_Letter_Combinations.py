# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150

#입력
#digits=input().strip()
digits="235"
numsOfCombi = len(digits)
#print(numsOfCombi)

#맵핑 정보를 딕셔너리로 저장
digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

#두 자릿수를 입력하면 두 자리 알파벳 조합
sizeOfList = len(digits)
resultList=[]

def Backtrack(digits, combi):

    #베이스 케이스: numsOfCombi자리수의 리스트를 다 채운 경우
    if(len(combi) == numsOfCombi):
        resultList.append(combi)
        #print(f'조합 추가{combi}')
        return 

    digit = digits[len(combi)] #숫자 하나 뽑기
    alphaString = digit_to_letters[digit] #수에 대응하는 문자열뽑기

    for alpha in alphaString:
        #1. 선택
        combi += alpha
    
        #탐색
        Backtrack( digits, combi)

        #취소
        combi = combi[:-1] #슬라이스로 뒤에서 한 글자 제거


#백트래킹 수행
Backtrack(digits, '')

print(resultList)