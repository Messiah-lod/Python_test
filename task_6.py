def __task_6__():
    print("Task 6")
    products = []
    for i in range(3):
        product_name = input("Введите название товара: ")
        product_price = input("Введите цену товара: ")
        try:
            product_price = int(product_price)
        except Exception:
            product_price = 0
        product_count = input("Введите количество товара: ")
        try:
            product_count = int(product_count)
        except Exception:
            product_count = 0
        product_measure = input("Введите единицы измерения товара: ")

        dict_product = {"Название": product_name, "Цена": product_price, "Количество": product_count,
                        "Ед": product_measure}
        tuple_product = (i + 1, dict_product)
        products.append(tuple_product)

    print("Исходная структура: ", products)

    dict_statistic = {}
    for product in products:
        for key in product[1]:
            value = dict_statistic.setdefault(key)
            if value is None:
                new_value = [product[1].get(key)]
                dict_statistic[key] = new_value
            else:
                value = list(value)
                if value.count(product[1].get(key)) == 0:
                    value.append(product[1].get(key))
                dict_statistic[key] = value

    print("Статистика: ", dict_statistic)
