import random
def randoms():
    numbers = list(range(1, 11))  
    q = random.choice(numbers)
    while True:
        a = int(input("1~10까지 수 중, 아무거나 선택 : "))
        if a == q:
            print('정답!')
            break
        else:
            print('오답!')
            if a in numbers:
                numbers.remove(a)
                print("범위를 좀 더 좁혀주겠습니다. ({0} 범위에서 삭제)".format(str(a)))
            elif a not in numbers:
                print("{0} 숫자는 범위에 없습니다.".format(str(a)))
randoms()