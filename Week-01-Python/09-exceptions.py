# Exceptions

# ZeroDivisionError
# 1 / 0

def divided_by(first, second):
    try:
        return first / second
    # except:
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다"

print(divided_by(4, 2))
print(divided_by(4, 0))

# 예외 만들기 - 개발자가 이런 에러가 나는 케이스는 있으면 안된다고 강조하는 경우
# Exception이라는 클래스가 있음
class EvenNumberDivisionError(Exception):
    pass

def divided_by_odd_numer(first, second):
    if second % 2 == 0:
        raise EvenNumberDivisionError
    else:
        return first / second

print(int(divided_by_odd_numer(6, 3)))
print(divided_by_odd_numer(6, 2))
