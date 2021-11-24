#ТерВер и МатСтат

import math
import numpy as np

#   Практическое задание №2 для 1 урока
#   Из ĸолоды в 52 ĸарты вынимают случайным образом 4 ĸарты.
#   Найти число исходов, соответствующих тому,
#   что был вытянут хотя бы один туз.
#
def combinations (n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n-k))

#   Возможно 4 варианта развития событий:
#   Выпадет 1 туз, 2 туза, 3 туза и 4 туза
#   вероятность получить туз равна сумме этих 4-х событий
#   P=P1+P2+P3+P4
P1 = combinations (4,1) * combinations (48,3)
P2 = combinations (4,2) * combinations (48,2)
P3 = combinations (4,3) * combinations (48,1)
P4 = combinations (4,4) * combinations (48,0)
#
#   P=P1+P2+P3+P4
p=P1+P2+P3+P4
print ('Задание №2')
print ('количество исходов',p)

