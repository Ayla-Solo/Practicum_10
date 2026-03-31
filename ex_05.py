def calculate_bonus(card_value):
    if card_value == 5 or card_value == 10:
        bonus = 0
    elif card_value == 25:
        bonus = 3
    elif card_value == 50:
        bonus = 8
    elif card_value == 100:
        bonus = 20
    else:
        raise ValueError("Недопустимое значение карты")

    return card_value + bonus


card_value = float(input("Введите стоимость: "))
print(calculate_bonus(card_value))