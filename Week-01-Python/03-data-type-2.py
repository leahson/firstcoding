# 목록 list, tuple
# 사전 dict - dictionary
# 집합 set

# list[] - 대괄호를 사용하는 것 만으로도 list라는 것을 인식함
# type는 ()안의 명령어의 클래스를 알려주는 명령어
print("list")
print([1, 2, 3])
# print(type([1, 2, 3]))
print(" ")
list_a = [1, 2, 3]
print(list_a)
# index는 '0'부터 시작. 이진수가 0, 1로 구성되어 있기 때문
print(list_a[0])
# slice는 index의 구간을 지정하여 나누는 것. 앞자리 숫자 자리는 포함, 뒷자리 숫자 자리는 불포함
print(list_a[0:2])
# .append()는 괄호 안의 숫자를 마지막 sequence에 추가
list_a.append(5)
print(list_a)
# remove()는 괄호 안의 숫자를 삭제
list_a.remove(2)
print(list_a)

# clear는 안에 들어 있는 모든 항목을 삭제
list_a.clear()
print(list_a)

# tuple (a, b, c) - 소괄호만 사용하는 것으로 tuple이라 인식 못하기 때문에 소괄호 안의 ,를 사용한 형식을 지켜야 함
# tuple과 list의 차이점 - tuple은 내부 값 추가/삭제가 불가능
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type(tuple_a))

# tuple_a.append(5) - error 명령어가 append 명령어가 존재하지 않음
# 그러면, 왜 구지 tuple 처럼 추가/삭제가 불가능한 명령어를 만들어 놓은 이유?
# 우선 프로그래밍 관점에서, 자원을 많이 활용하고 있는 것
# 1) 추가 명령어 ex. append()를 사용하지 않을 경우에는 tuple이 성능이 더 좋음 (간단)
# 2) 의도적으로 값을 바뀌면 안되게 하기 위함

# dict(map) {}
# 가장 중요한 점 - key : value로 구성되어 있다는 점
dict_a = {
    "apple" : "a type of fruits",
    "pen" : "a thing to write"
}
print(dict_a)
print(dict_a["apple"])
# edit value
dict_a["pen"] = "something to write"
print(dict_a)

# set set([]) - 집합
# 사용 경우 - 중복이 없이 처리해야하는 경우. 중복이 자동으로 제거됨!!!
set_a = set([1, 2, 3, 3, 3])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)

# 집합의 종류 - 교집합, 합집합, 차집합, 여집합
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
