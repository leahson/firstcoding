# 참과 거짓 판단 boolean
# if
# True, False
# and, or, not

a = True
b = False

# A 가 참이거나 혹은 B가 참이라면 (A나 B 둘 중에 하나라도 참이면 된다)
print(a and b)
# A 가 참이고 그리고 B가 참이라면 (A와 B 둘 다 참이어야 한다)
print(a or b)

# == 뒤의 값과 동일 한가?
# = 는 값을 할당 하는 것
c = True
print(c == True)
print(c is True)

d = 7
if d > 10:
    print("숫자는 10보다 큽니다")
elif d > 5 and d <= 10:
    print("숫자는 10보다 작거나 같고, 5보다는 큽니다")
else:
    print("숫자는 5보다 작습니다")
