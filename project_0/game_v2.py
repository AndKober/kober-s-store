"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def predict(number: int = 1) -> int:
    """Угадываем число, сужая диапазон угадывания в двое на каждом цикле

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    minimal = 1
    maximal = 101
    
    while True:
        count += 1
        predict_number = int((maximal+minimal)/2) # предполагаемое число всегда в центре диапазона
        if number > predict_number:
            minimal = predict_number 
        elif number < predict_number:
            maximal = predict_number 
        else:
            break  # выход из цикла если угадали
    return count


def score_game(predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict)
