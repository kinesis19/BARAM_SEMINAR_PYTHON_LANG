class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def add_student():
    name = input("학생의 이름을 입력하세요: ")
    age = int(input("학생의 나이를 입력하세요: "))
    grade = input("학생의 학년을 입력하세요: ")
    student = Student(name, age, grade)
    return student

def search_student(student_list, name):
    for student in student_list:
        if student.name == name:
            return student
    return None

def display_student_info(student):
    if student:
        print("학생 정보:")
        print(f"이름: {student.name}")
        print(f"나이: {student.age}")
        print(f"학년: {student.grade}")
    else:
        print("해당 학생을 찾을 수 없습니다.")

def main():
    student_list = []

    while True:
        print("\n1. 학생 추가")
        print("2. 학생 검색")
        print("3. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == "1":
            student = add_student()
            student_list.append(student)
            print("학생이 추가되었습니다.")
        elif choice == "2":
            name = input("검색할 학생의 이름을 입력하세요: ")
            found_student = search_student(student_list, name)
            display_student_info(found_student)
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

main()
