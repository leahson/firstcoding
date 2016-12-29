# 구현 내용
#
# 앞서 중간 점검 때 공부했던 구구단이 사용자가 어떤 다른 값을 넣더라도 에러가 나지 않도록 처리해 봅시다.
# (추가 과제에서 2~9라는 숫자 외에는 구구단이 출력하지 않도록 처리했습니다.)
# 예를 들어, 현재 숫자가 아닌 "1단"이라는 문자를 넣으면 구구단이 실행되지 않고 종료됩니다.
# 잘못된 값을 입력한 경우, "2에서 9사이의 숫자만 입력해주세요."이라는 문구와 함께 다시 구구단이 실행되도록 합시다.
# 힌트
#
# 에러 처리를 이용합니다.
# 함수 안에 동일한 함수를 다시 호출할 수 있습니다. 검색 키워드: 재귀 함수 recursive

def gugudan():
    try:
        question = int(input("2에서 9 사이의 숫자를 입력해주세요: "))
        if question > 1 and question < 10:
            for num in range(1, 10):
                print("{} * {} = {}".format(question, num, question * num))
        else:
            print ("2에서 9 사이의 숫자만 입력해주세요!!")
            gugudan()
    except ValueError:
        print("숫자만 입력해주세요.")
        gugudan()
    except:
        print("알 수 없는 에러가 발생하였습니다.")
        gugudan()

gugudan()
