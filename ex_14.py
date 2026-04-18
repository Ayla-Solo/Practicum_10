def first_match(target, pattern, start = 0, end = None):
    if end is None:
        end = len(target)

    # Если пустая возвращаем start
    if not pattern:
        return start if start <= end else -1

    # Если длина шаблона больше доступной области поиска невозможно
    if len(pattern) > end - start:
        return -1

    # Создаем таблицу сдвигов
    shifts = {b: i for i, b in enumerate(pattern)}
    # Начинаем сравнение с конца шаблона
    i = start + len(pattern) - 1
    while i < end:
        j = len(pattern) - 1  

        while j >= 0 and target[i - (len(pattern) - 1) + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i - len(pattern) + 1

        # Берем символ на котором произошел разрыв
        bad_char = target[i]

        # Вычисляем сдвиг по правилу плохого символа
        shift = j - shifts.get(bad_char, -1)

        # Смещаем окно поиска
        i += max(1, shift)

    # Если совпадений нет возвращаем -1
    return -1


def boyer_moore_positions(target, pattern, start = 0, end = None):
    if end is None:
        end = len(target)

    if not pattern:
        return ','.join(str(i) for i in range(start, min(end, len(target))))

    positions = []  # список найденных позиций
    pos = start     # текущая позиция поиска

    # Ищем все вхождения
    while pos < end:
        match_pos = first_match(target, pattern, pos, end)
        # Если больше совпадений нет — выходим
        if match_pos == -1:
            break

        positions.append(match_pos)

        # Сдвигаемся на 1 символ вправо 
        pos = match_pos + 1

    # Возвращаем позиции в виде строки через запятую
    return ','.join(str(p) for p in positions)

print(first_match("ATGCAATCG", "ATC"))        # первое вхождение
print(boyer_moore_positions("ATCATCATC", "ATC"))  # все вхождения
