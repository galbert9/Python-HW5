#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Не понял даже смысл задачи, просто скопировал код

data = [1,2,3]

def encode(data):
    encoding = ' '
    ex = ' '
    count = 1
    if not data: return ' '
    for el in data:
        if el != ex:
            if ex:
               encoding += str(count) + ex
            count  = 1
            ex = el
        else:
            count += 1
    else:
        encoding += str(count) + ex
        return encoding

    