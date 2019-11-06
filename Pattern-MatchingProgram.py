import sys

def printMenu(): # 메뉴를 출력해주는 함수
    print('\n--------------------------------')
    print('1 : 패턴 매칭 프로그램 시작')
    print('2 : 프로그램종료')
    choice = input('Enter your choice: ')
    return choice

def inputData(): # 사용자에게 문자열과 패턴을 입력받는 함수
    while True:
        S = input('문자열을 입력하세요 : ')
        n = len(S)
        if n > 10: # 문자열의 길이가 제한을 넘으면
            print('문자열의 길이는 10자리 까지입니다. 다시입력하세요.')
        else:
            P = input('찾을 패턴을 입력하세요 : ')
            m = len(P)
            if m > 3: # 패턴의 길이가 제한을 넘으면
                print('찾을 수 있는 패턴의 길이는 3자리 까지입니다. 다시입력하세요.')
            else:
                position = match(P, S, n, m) # 패턴위치 저장
                if position == 0: # 문자열보다 패턴의 길이가 클시
                    print('문자열보다 패턴의 길이가 큽니다.')
                else:
                    print('패턴의 위치는 %d입니다.'% position)
                break

def match(P, S, n, m): # 패턴 매칭 알고리즘을 적용한 함수, 패턴 위치 함수
    l = 0 # 패턴의 시작 위치
    matched = False
    if (m >= 1) and (n >=1) and (m > n): # 문자열보다 패턴의 길이가 크다면
        return 0
    while l <= n - m and matched == False:
        l = l + 1
        r = 0 # 검색하고 있는 위치를 임시 저장
        matched = True
        while r < m and matched == True:
            matched = matched and P[r] == S[l+r-1] # 배열에서는 인덱스가 0부터
            r = r + 1
    return l

if __name__ == '__main__':
    print('Pattern-Matching Program')
    while True:
        choice = printMenu()
        if choice == '1':
            inputData()
        elif choice == '2':
            print('Thank you for using this program')
            sys.exit(1)
        else:
            print('invalid choice')