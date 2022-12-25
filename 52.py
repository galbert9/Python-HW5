# Создайте программу для игры в "Крестики-нолики"

# список в списке (строки, столбец, две диагонали)
field = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6],]
#for i in field:
    #print(i)   
    # print()
    #print(list[i[0]])

def game(name1, name2):
    win = " "
    for i in field:
        if list[i[0]] == "x" and list[i[1]] == "x" and list[i[0]] == "x":
            win = name1
        if list[i[0]] == "0" and list[i[1]] == "0" and list[i[0]] == "0":
            win = name2
    print(win)        


 # def game(field):
#     if field[0][0] == field [1][0] == field [2][0] != '+':
#         return f'выиграл field [0]'