# 예외처리 종류 및 사용 예시
try:
    # 예외가 발생할 수 있는 코드 블록
    x = int(input("나눌 숫자를 입력하세요: "))
    y = int(input("나누어지는 숫자를 입력하세요: "))
    result = x / y
except ValueError:
    # 입력이 잘못되었을 때의 예외 처리
    print("잘못된 입력입니다. 숫자를 입력하세요.")
except ZeroDivisionError:
    # 0으로 나누려고 했을 때의 예외 처리
    print("0으로 나눌 수 없습니다.")
else:
    # 예외가 발생하지 않았을 때의 코드 블록
    print("나눗셈 결과: ", result)
finally:
    # 예외 발생 여부에 관계없이 항상 실행되는 코드 블록
    print("프로그램을 종료합니다.")