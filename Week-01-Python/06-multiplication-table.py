# 추가과제 = 구구단을 출력해 봅시다
question = int(input("몇 단을 출력 하시겠습니까?"))
for num in range(1, 10):
    print("{} * {} = {}".format(question, num, question * num))
