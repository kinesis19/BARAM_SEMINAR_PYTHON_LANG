def find_max(*numbers):
    if len(numbers) == 0:
        return None
    else:
        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
        return max_num

def get_numbers_from_user():
    numbers = []
    while True:
        try:
            num = float(input("Enter a number (or press Enter to finish): "))
            numbers.append(num)
        except ValueError:
            break
    return numbers

def display_result(max_number):
    if max_number is None:
        print("No numbers were entered.")
    else:
        print("The maximum number is:", max_number)

user_numbers = get_numbers_from_user()

max_value = find_max(*user_numbers)

display_result(max_value)