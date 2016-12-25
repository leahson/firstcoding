# 서울의 맛집을 추천해 드립니다.

restotype = input("한식, 일식, 중식 중 하나를 선택하세요:")

import random
Korean = [
    "정식당 - 서울시 강남구 청담동 선릉로 158길 11 (02-517-4654)",
    "석파랑 - 서울시 종로구 홍지동 125 (02-395-2500) ",
    "삼청각 - 서울시 성북구 성북동 330-115 (02-765-3700)"
]
Japanese = [
    "쥬안 - 서울 강남구 압구정로72길 12 (02-512-4833)",
    "아리아케 - 서울시 중구 장충동 동호로 249 (02-2230-3356)",
    "스시 코마츠 - 서울시 강남구 신사동 624-19 (02-515-1177)"
]
Chinese = [
    "유유안 - 서울시 종로구 새문안로 97 (02-6388-5000)",
    "신성각 - 서울시 마포구 신공덕로 2-463 (02-716-1210)",
    "파크루안 - 서울시 강남구 논현로 430 아세아타워빌딩 지하 1층 (02-562-5565)"
]

if restotype == "한식":
    random.shuffle(Korean)
    print(Korean.pop())

elif restotype == "일식":
    random.shuffle(Japanese)
    print(Japanese.pop())

elif restotype == "중식":
    random.shuffle(Chinese)
    print(Chinese.pop())

else:
    print("Error - 한식, 일식, 중식 중 한 가지를 고르세요.")
