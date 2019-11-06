# 2014152039 최진혁
# -*- coding: utf-8 -*-
import sys # exit()를 위해 임포트

def inputdata(): # 양의 정수 입력 받는 함수
    icommand = input('Enter an unsigned integer : ') # 양의 정수 저장
    if icommand == 'stop': # 정수가 아닌 'stop' 입력시 함수 종료
        print('Thank you for using this program\n')
        sys.exit(1)
    elif icommand.isdigit() == True: # 입력받은 문자열이 숫자이면 True
        data = int(icommand) # 문자열을 정수로 형변환
        system(data) # system 함수 호출
    else: # 정수가 아닐시 계속 호출
        inputdata()


def system(data): # 변환할 진법 고르는 함수
    scommand = input('b or B for binary, o or O for octal, h or H for hexadecimal : ') # 커맨드 저장
    if scommand == 'b' or scommand == 'B': # 2진법 변환
        print(change(data, 2)) # 변환함수 호출
    elif scommand == 'o' or scommand == 'O': # 8진법 변환
        print(change(data, 8)) # 변환함수 호출
    elif scommand == 'h' or scommand == 'H': # 16진법 변환
        print(change(data, 16)) # 변환함수 호출
    else: # 잘못된 커맨드 입력시
        print('Invalid choice!')
        system(data) # system 함수 호출
    print('==================================================================\n')
    inputdata() # 다시 inputdata 함수 호출

def change(n, base): # 변환 함수
    L = "0123456789ABCDEF" # 변환시 문자열의 index를 이용해 매칭
    q, r = divmod(n, base) # n을 base로 나눈 몫과 나머지를 튜플 형태로 저장 q : 몫, r : 나머지
    if q == 0: # 몫이 0일때
        return L[r] # r은 index로 사용
    else: # 몫이 0이 아니라면 변환함수 호출
        return change(q, base) + L[r] # 나머지들을 거꾸로 모음

if __name__ == '__main__':
    print('This program will convert a base 10 number into another base')
    inputdata() # inputdata 함수 호출