# 함수 functions - 중복값을 단순하게 만들어 준다. 수정시 간편하다.
# 입력값 parameters, 반환값 return

# def - definition 함수 지정 
def hello_friends(name):
    print("Salut, {}".format(name))

name1 = "Marco"
name2 = "Jane"
name3 = "John"
name4 = "Tom"
name5 = "Léa"
name6 = "Olivier"
name7 = "Marc"
name8 = "Noreen"

# 함수를 사용하지 않고 개별 명령어를 사용한 후, 수정이 필요하게 되면 각 명령어를 모두 고쳐야 하는 불편함이 발생
# print("hi, {}".format(name1))
# print("hi, {}".format(name2))
# print("hi, {}".format(name3))
# print("hi, {}".format(name4))
# print("hi, {}".format(name5))
# print("hi, {}".format(name6))
# print("hi, {}".format(name7))
# print("hi, {}".format(name8))


hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)

# 입력값 o, 반환값 o
def sum(a, b):
    return a + b

# 입력값 o, 반환값 x
def hello_friends(name):
    print("Salut, {}".format(name))

# 입력값 x, 반환값 o
def return_1():
    return 1

num1 = return_1() # 반환값이 있다는 것은 변수에 담을 수 있다는 의미
print(num1)

# 입력값 x, 반환값 x
def hello_world():
    print("hello world")
