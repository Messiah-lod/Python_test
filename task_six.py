import main


def __task_six__():
    print("**********  Task 6  **********")
    first_day = main.__checking_for_number__("Введите результат первого дня в км: ")
    second_day = main.__checking_for_number__("Введите желаемый результат в км: ")
    if second_day < first_day:
        print("Вы достигли результатов, поздравляем!")
        return

    result = first_day
    count_day = 1
    while result < second_day:
        result *= 1.1
        count_day += 1
        print(f"Результат {count_day} дня: {round(result, 2)}")
    print(f"На {count_day} - й день спортсмен достиг результата — не менее {second_day} км")
