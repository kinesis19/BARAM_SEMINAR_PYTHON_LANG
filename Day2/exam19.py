# 가변인자 활용 예시
def add(a, b, *numbers):
    result = a + b
    for num in numbers:
        result += num
    return result

result = add(3, 4, 5, 6, 7)
print(result)