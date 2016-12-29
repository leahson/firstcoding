# 클래스 Class

##### Article variables
title1 = "개발"
author1 = "마르코"
content1 = "개발은 쉬워요"
view_count1 = 0

title2 = "창업"
author2 = "마르코"
content2 = "창업은 쉬워요"
view_count2 = 0

title3 = "코칭"
author3 = "마르코"
content3 = "코칭은 쉬워요"
view_count1 = 0

##### Article Class
# class Article:
#     title = "개발"
#     author = "마르코"
#     content = "개발은 쉬워요"
#     view_count = 0
#
## 클래스 활성화를 시켜야 한다. 변수 = 클래스 ()
# article1 = Article()
# print(article1.title)
# article2 = Article()
# print(article2.author)
# article2.title = "코칭"
# print(article1.title)
# print(article2.title)

##### Article class with __init__
class Article:
    author = "마르코"
    view_count = 0

# self - class 안에 있는 변수에 접근하겠다는 의미 (class 내 함수)
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

# 클래스 활성화 시, init 함수가 있으면 순서대로 함수 값을 넣어주어야 한다.
article1 = Article("개발", "개발은 쉬워요")
article2 = Article("코칭", "코칭은 쉬워요")
article3 = Article("창업", "창업은 쉬워요")

print("블로그 분류: " + article1.title)
print(article1.view_count)
article1.read()
# read() 함수를 지정하지 않았을 경우, 아래 함수를 반복했어야 한다
# article1.view_count = article1.view_count + 1
print(article1.view_count)

##### Article class inheritance 상속
class BrunchArticle(Article):
    source = "브런치"

    def read(self):
        self.view_count = self.view_count + 2
        # 부모 함수의 것을 그대로 가져올 수 있고 새로 정의 수 있다 = over write

brunch_article = BrunchArticle("개발", "개발은 쉬워요")
print(brunch_article.title)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)
