def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for elem in numbers:
        try:
            result += elem
        except TypeError:
            print(f'Некорректный тип данных для подсчета суммы - {elem}')
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        summ, incorrect = personal_sum(numbers)
        result = summ / (len(numbers) - incorrect)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных.")
        return None
    return result

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')