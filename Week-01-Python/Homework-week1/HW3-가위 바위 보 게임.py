# 가위 바위 보 게임을 해봅시다.

# - 사용자에게 가위, 바위, 보 중 하나를 물어봅니다.
# - 사용자가 가위, 바위, 보 중 하나를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
# - 다 합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.

# 힌트
# - 리스트를 한 개 사용하고, 사용자의 입력을 받아야 합니다.
# - 앞서 사용했던 임의 뽑기를 다시 사용합니다.
# - 검색 키워드 : random, randint, shuffle
# - 컴퓨터에게 가위, 바위, 보의 승패를 가르쳐줘야 합니다.

# 변수로 지정해 두면, 파이썬은 변수 인식 에러가 있을 경우 알려주기 때문에 편하다.

import random

Rock = "바위"
Scissors = "가위"
Paper = "보"
RSP_LIST = (
    Rock,
    Scissors,
    Paper
)

win_count = 0
lose_count = 0

while win_count < 3 and lose_count < 3:
# 1) 사용자 입력
    user_choice = input("{}, {}, {} 중 하나를 선택하세요:".format(
        Scissors, Rock, Paper
    ))
# 2) 컴퓨터 임의 선택
    computer_choice = random.choice(RSP_LIST)
# 3) 3번 지거나 이기면 승패 확정
    if user_choice == computer_choice:
        print(computer_choice)
        print("비겼습니다.")
    elif user_choice not in RSP_LIST:
        print("가위, 바위, 보 중에서 하나를 입력해 주세요.")
    elif((user_choice == Rock and computer_choice == Scissors)
        or (user_choice == Scissors and computer_choice == Paper)
        or (user_choice == Paper and computer_choice == Rock)):
        win_count = win_count + 1
        print(computer_choice)
        print("이겼습니다.")
    else:
        lose_count = lose_count + 1
        print(computer_choice)
        print("졌습니다.")

if win_count == 3:
    print("사용자가 최종 승리하였습니다.")
else:
    print("컴퓨터가 최종 승리하였습니다.")
