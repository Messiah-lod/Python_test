def __task_5__():
    print("Task 5")

    rating = [7, 5, 3, 3, 2]
    #    help(rating)
    for i in range(5):  # добавим 5 числе в исходную последовательность

        while True:
            answer = input("Введите число для рейтинга: ")
            try:
                user_number = int(answer)
                break
            except Exception:
                print("Введен не верный формат данных, попробуйте еще раз.")

        if len(rating) < 1:
            rating.append(user_number)
        elif user_number < rating[-1]:
            rating.append(user_number)
        elif rating.count(user_number) == 0:
            for k in range(len(rating)):
                if user_number > rating[k]:
                    rating.insert(k, user_number)
                    break
        else:
            insert_index = rating.index(user_number) + rating.count(user_number)
            rating.insert(insert_index, user_number)

        print(rating)
