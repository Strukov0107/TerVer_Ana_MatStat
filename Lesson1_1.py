#ТерВер и МатСтат

import math
import numpy as np

#   Практическое задание №1 для 1 урока
#   Группа студентов изучает 10 различных дисциплин.
#   Сĸольĸими способами можно составить расписание
#   на понедельниĸ, если в этот день должно быть 4 разных
#   занятия?

def arrangements (n,k):
  return np.math.factorial (n) // np.math.factorial (n - k)
print ('Задание №1')
print ('расписание можно составить', arrangements (10,4), 'вариантами')



