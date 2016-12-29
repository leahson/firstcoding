# for (~하는 동안), range(a, b) - b는 불포함
# while (~하는 동안) - for와 용법이 다름

# for
for num in range(1, 10): # cf. [1, 2, 3][0:2]
    print(num)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in num_list:
    print(num)

# while
# while True: # 무한루프 - while의 특성이 False로 바뀔때까지 계속 출력
#     print(1)
# 끝내려면 cmd + c

a = 1
while a < 10:
    print(a)
    a = a + 1
