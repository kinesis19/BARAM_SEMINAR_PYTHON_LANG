# 키워드 인자(Keyward argument) 예시
def greet(**kwargs):
    for key in kwargs:
        print(f'key: {key}, value : {kwargs[key]}')

greet(name = "영희", age = 25)
greet(age = 30, name = "철수")