import sys

def greeting(): # 프로그램 사용 감사 출력 함수
    print('Welcome to the bookstore program!')

def readDatabase(theInventory): # 사용자에게 입력파일명을 요구하고, 입력파일의 데이터를 Dictionary 구조로 만드는 함수
    filename = input('Enter the name of the file: ') # 입력파일명 저장
    key = [] # 딕셔너리에 들어갈 키값들만 모아두는 리스트
    value = [] # 딕셔너리에 들어갈 벨류값들만 모아두는 리스트
    data = [] # 입력파일의 데이터들을 저장할 리스트
    storeDatas(filename, data)
    size = len(data)
    for i in range(0, size): # 데이터 총 사이즈 까지
        key.append(data[i][0] + ', ' + data[i][1]) # lastname, firstname 순으로 키값 저장
        value.append(data[i][2] + ',' + data[i][3] + ',' + data[i][4]) # title,qty,price 순으로 벨류값 저장
        theInventory[key[i]] =  [] # 딕셔너리 각 키값의 벨류값을 이중리스트로 저장
    for i in range(0, size):
        theInventory[key[i]].append([value[i]]) # 딕셔너리 각 키값에 맞는 벨류값에 리스트 형태의 데이터 저장

def printMenu(): # 사용자 메뉴를 출력하는 함수로 사용자의 choice를 리턴함
    print('\n--------------------------------')
    print('Enter 1 to display the inventory')
    print('Enter 2 to display the books by one author')
    print('Enter 3 to add a book')
    print('Enter 4 to change the price')
    print('Enter 5 to change the qty on hand')
    print('Enter 6 to view the total number of books in the inventory')
    print('Enter 7 to see the total amount of the entire inventory')
    print('Enter 8 to exit')
    choice = input('Enter your choice: ')
    return choice

def displayInventory(theInventory): # 재고를 출력하는 함수로 저자의 정렬 순으로 출력하며 저자 별로는 책 제목 순으로 정렬 된 정보를 출력해줌
    author = sorted(theInventory.keys()) # 정렬된 저자들을 리스트로 저장
    for i in range(0, len(author)): # 총 저자들 수 까지
        print('The author is: ' + author[i])
        sortedvalues = sorted(theInventory[author[i]]) # 정렬된 벨류값들을 리스트로 저장
        printValues(sortedvalues) # 벨류값들 출력하는 함수 호출

def displayAutorsWork(theInventory): # 사용자에게 저자명(last name과 first name)을 요구하고 그 저자의 책 정보를 제목으로 정렬된 순으로 출력해 줌. 만약 사용자가 요청한 저자가 정보에 없다면 적절한 출력을 해줘야 함
    firstname, lastname = nameInput() # 저자명을 입력받는 함수
    author = theInventory.keys() # 딕셔너리의 키값들 저장
    if ((lastname + ', ' + firstname) in author) == False: # 입력받은 저자명이 딕셔너리 키값들에 속하지 않는다면
        print('Sorry, but no books by ' + lastname + ', ' + firstname + ' in the inventory')
        return
    else: # 입력받은 저자명이 키값들에 속할때
        sortedvalues = sorted(theInventory[lastname + ', ' + firstname])  # 정렬된 벨류값들을 리스트로 저장
        printValues(sortedvalues) # 벨류값들 출력하는 함수 호출


def addBook(theInventory): # 사용자에게 저자명, 책제목, 재고량, 그리고 책 가격을 요구하여 만약 저자가 존재하고, 새 책일 경우 정보를 저장하고 이미 존재 한다면, 적절한 출력을 해 줘야 함. 만약 저자가 존재하지 않다면, theInvetory에 새로운 원소(저자명)가 추가되어 그 저자 에 대한 정보로 저장되어야 함. 재고량은 정수로 입력되어야 하며, 가격은 양의 실수로 입력되어야 함
    firstname, lastname = nameInput() # 저자명을 입력받는 함수
    title = input("Enter the title: ") # 책제목 저장
    title = title.title() # 띄어쓰기 구분하여 각 앞글자 모두 대문자로 변환
    titles = [] # 책제목들 넣어둘 리스트
    author = list(theInventory.keys()) # 저자들을 리스트로 저장
    for i in range(0, len(author)): # 총 저자들 수 까지
        listvalues = list(theInventory[author[i]]) # 벨류값들을 리스트로 저장
        for listvalue in listvalues:
            value = listvalue[0].split(',')
            titles.append(value[0]) # 책제목 모으기
    if (((lastname + ", " + firstname) in theInventory.keys()) == True) and ((title in titles) == True): # 책이 존재한다면
        return print('This book is already in the Inventory and cannot be added again')
    else:
        while True: # 재고량 입력
            qty = input("Enter the qty: ")
            if qty.isdecimal() == False: # 재고량이 양의 정수가 아니라면
                print('Invalid input for qty.')
            else:
                break
        while True: # 가격 입력
            price = input("Enter the price: ")
            if isfloat(price) == False: # 가격이 양의 실수가 아니라면(둘째자리까지)
                print('Invalid input for price.')
            else:
                break
    if ((lastname + ", " + firstname) in theInventory.keys()) == True: # 책의 저자가 존재한다면 책의 정보를 저장
        theInventory[lastname + ', ' + firstname]  = theInventory[lastname + ', ' + firstname] + [[title + ',' + qty + ',' + price]]
    else: # 책의 저자가 존재하지 않다면 새로 등록
        theInventory[lastname + ", " + firstname] = [[title + ',' + qty + ',' + price]]

def changePrice(theInventory): # 사용자에게 가격정보를 변경하기 위해 필요한 저자의 이름과 책 제목을 요구 하고, 양의실수로 입력될 때만 가격을 변경해 줌. 만약 저자나 혹은 책제목이 존재 하지 않을 경우 적절한 출력 메시지 필요
    firstname , lastname = nameInput() # 저자명을 입력받는 함수
    if ((lastname + ", " + firstname) in theInventory.keys()) == False: # 입력받은 책의 저자가 딕셔너리에 없을시
        print('No such author in your database. So you cannot change the price')
    else: # 저자명이 존재할때
        listvalues = list(theInventory[lastname + ', ' + firstname]) # 해당하는 키값의 벨류값들을 리스트로 저장
        title = input("Enter the title: ") # 책제목 저장
        title = title.title() # 띄어쓰기 구분하여 각 앞글자 모두 대문자로 변환
        titles = [] # 책제목들 넣어둘 리스트
        for listvalue in listvalues:
            value = listvalue[0].split(',')
            titles.append(value[0]) # 책제목 모으기
            if value[0] == title: # 책제목이 존재한다면 재고량과 가격을 불러옴
                qty = value[1]
                price = value[2]
        if (title in titles) == False:  # 책제목과 일치하는 것이 없다면
            print('No book with the title ' + title + ' by' + lastname + ', ' + firstname + ' in inventory.')
        else:  # 책제목과 일치하는 것이 있다면
            while True:
                newprice = input("Enter the price: ")  # 새로운 가격 입력 저장
                if isfloat(newprice) == False:  # 소수점둘째짜리까지의 실수인지 검사했을때 아니라면
                    print('Invalid input for the new price.')
                else:  # 맞는 가격을 입력했다면 원래가격에서 새로운 가격으로 수정
                    print('Price will be updated from ' + price + ' to ' + newprice)
                    olddata = [title + ',' + qty + ',' + price]  # 원래 정보
                    listvalues.remove(olddata)  # 원래 정보 제거
                    theInventory[lastname + ', ' + firstname] = listvalues + [
                        [title + ',' + qty + ',' + newprice]]  # 딕셔너리에 새로운 정보 추가(수정)
                    break



def changeQty(theInventory): # 위 changePrice와 같은 기능을 하나 가격이 아닌 재고량을 변경해 주는 기능 을 함. 항상 양의 정수를 입력 받아야 함
    firstname, lastname = nameInput()  # 저자명을 입력받는 함수
    if ((lastname + ", " + firstname) in theInventory.keys()) == False: # 저자명이 딕셔너리에 없다면
        print('No such author in your database. So you cannot change the qty')
    else: # 저자명이 존재한다면
        listvalues = list(theInventory[lastname + ', ' + firstname]) # 해당하는 키값의 벨류값들을 리스트로 저장
        title = input("Enter the title: ") # 책제목 저장
        title = title.title() # 띄어쓰기 구분하여 각 앞글자 모두 대문자로 변환
        titles = [] # 책제목들 넣어둘 리스트
        for listvalue in listvalues:
            value = listvalue[0].split(',')
            titles.append(value[0]) # 책제목 모으기
            if value[0] == title: # 책제목이 존재한다면 재고량과 가격을 불러옴
                qty = value[1]
                price = value[2]
        if (title in titles) == False:  # 책제목과 일치하는 것이 없다면
            print('No book with the title ' + title + ' by' + lastname + ', ' + firstname + ' in inventory.')
        else:  # 책제목과 일치하는 것이 있다면
            while True:
                newqty = input("Enter the qty: ")  # 새로운 재고량 입력 저장
                if newqty.isdecimal() == False:  # 양의 정수인지 검사시 아니라면
                    print('Invalid input for the new price.')
                else:  # 양의 정수라면 원래 재고량에서 새로운 재고량으로 수정
                    print('Qty will be updated from ' + qty + ' to ' + newqty)
                    olddata = [title + ',' + qty + ',' + price]
                    listvalues.remove(olddata)
                    theInventory[lastname + ', ' + firstname] = listvalues + [[title + ',' + newqty + ',' + price]]
                    break

def totalQty(theInventory): # 재고에 있는 모든 책의 개수를 계산하여 출력해 줌
    author = list(theInventory.keys()) # 저자들을 리스트로 저장
    sum = 0 # 합을 저장할 변수
    for i in range(0, len(author)):
        listvalues = list(theInventory[author[i]]) # 벨류값들을 리스트로 저장
        for listvalue in listvalues:
            value = listvalue[0].split(',')
            sum += int(value[1]) # 재고량만 더함
    print('%d' % sum) # 합 출력

def calculateTotalAmount(theInventory): # 재고에 있는 모든 책의 가격을 합산하여 출력해 줌
    author = list(theInventory.keys()) # 저자들을 리스트로 저장
    sum = 0 # 합을 저장할 변수
    for i in range(0, len(author)):
        listvalues = list(theInventory[author[i]])  # 벨류값들을 리스트로 저장
        for listvalue in listvalues:
            value = listvalue[0].split(',')
            sum += float(value[2])*float(value[1]) # 곱의 합
    print('%0.2f' %sum) # 소수점 둘째짜리까지 합 출력

def storeDatas(filename, data): # 입력파일 데이터를 저장하는 함수
    if filename == 'database.txt': # 입력파일명이 databas.txt 이라면
        with open('database.txt', 'r') as f:
            for line in f.readlines():
                lines = line.strip().split(',') # 공백제거 및 ',' 제거
                data.append(lines) # 데이터 저장
        return data
    else:  # 입력파일명 다를시 다시 readDatabase 호출
        print('Error reading database')
        readDatabase(theInventory)

def printValues(sortedvalues): # 벨류값들을 출력해주는 함수
    for sortedvalue in sortedvalues:
        value = sortedvalue[0].split(',')
        print('\tThe title is: ' + value[0])  # title
        print('\tThe qty is: ' + value[1])  # qty
        print('\tThe price is: ' + value[2])  # price
        print('\t____')

def nameInput(): # 저자명을 입력받는 함수
    firstname = input("Enter the author's first name: ")  # first name 저장
    lastname = input("Enter the author's last name: ")  # last name 저장
    firstname = firstname.lower()  # firstname 모두 소문자로 변환
    firstname = firstname.capitalize()  # firstname의 앞글자만 대문자로 변환
    lastname = lastname.lower()  # lastname 모두 소문자로 변환
    lastname = lastname.capitalize()  # lastname의 앞글자만 대문자로 변환
    return firstname, lastname

def isfloat(num): # 소수점둘째짜리까지의 실수인지 검사
    a, _, b = num.partition('.')
    if (a.isdecimal() == True) and (b.isdecimal() and (len(b) == 2)): # 소수점 앞은 양의정수, 소수점뒤는 양의정수에 소수둘째짜리까지
        return True
    else:
        return False

if __name__ == '__main__':
    greeting()
    theInventory = {}
    readDatabase(theInventory)
    while True:
        choice = printMenu()
        if choice == '1':
            displayInventory(theInventory)
        elif choice == '2':
            displayAutorsWork(theInventory)
        elif choice == '3':
            addBook(theInventory)
        elif choice == '4':
            changePrice(theInventory)
        elif choice == '5':
            changeQty(theInventory)
        elif choice == '6':
            totalQty(theInventory)
        elif choice == '7':
            calculateTotalAmount(theInventory)
        elif choice == '8':
            print('Thank you for using this program')
            sys.exit(1)
        else:
            print('invalid choice')
