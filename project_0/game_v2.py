"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    count = 0
    number = np.random.randint(1, 101)
    min = 0
    max = 100
    while True:
        predict = round((min+max)/2)
        count += 1
        if number == predict:
             break
        elif number > predict:
            min = predict
      
        elif number < predict:
            max = predict
     
    return(count)


def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
        
if __name__ == "__main__":
    score_game(random_predict)