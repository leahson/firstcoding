# 회사 조직도를 만들어 보겠습니다.

##### 사람 클래스 - 기본 요소 이름, 나이, 성별 포함
class Man:
    name = input("이름을 입력하세요: ")
    age = input("나이를 입력하세요: ")
    sex = input("성별을 선택하세요 - 남자 또는 여자: ")

class WithPosition(Man):
    position = "대리"

class Man(WithPosition):
    def read(self):
        self.position = input("직급을 다시 입력하세요: ")

man1 = Man()
print(man1.name)
print(man1.age)
print(man1.sex)
print(man1.position)
man1.read()
print(man1.name)
print(man1.age)
print(man1.sex)
print(man1.position)
