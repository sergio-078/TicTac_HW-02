hello = 3 # размер игрового поля 3 на 3
matrix_hello = []

print('Вашему вниманию предложена игра крестики-нолики на игровом поле размером 3 на 3!\n'
      'Игроки ходят по очереди, первым начинает крестик (Х).')

#функция формирования квадратной матрицы по размеру, согласно переменной 'hello'):
def matrix_hello_func():
    k, t = 0, 0

    #строим матрицу, равную переменной 'hello' и заполняем элементами '-'
    for i in range(hello+1):
        row = []
        for j in range(hello+1):
            row.append('-')
        matrix_hello.append(row)

    #нумеруем строки и столбцы игрового поля:
    for i in range(hello+1):
        matrix_hello[0][i] = k
        k += 1
    for i in range(hello+1):
        matrix_hello[i][0] = t
        t += 1

    #вместо '0' в клетке 0:0 отобразим пустую ячейку ' ':
    matrix_hello[0][0] = ' '


#функция построения матрицы в нужном виде (отображении):
def matrix_func():
    for row in matrix_hello:
        for element in row:
            print(element, end=" ")
        print()


# функция ввода данных в нужном формате
def data_control(row=0, col=0):
    pattern1, pattern2, pattern3 = '1:1', '1:2', '1:3'
    pattern4, pattern5, pattern6 = '2:1', '2:2', '2:3'
    pattern7, pattern8, pattern9 = '3:1', '3:2', '3:3'

    x = input()

    if x != pattern1 and x != pattern2 and x != pattern3 and x != pattern4 and x != pattern5 and x != pattern6 and x != pattern7 and x != pattern8 and x != pattern9:
        print('Ошибка, Вы ввели значение клетки не в верном формате!')
        return data_control(row, col)
    else:
        row = int(x[:1])
        col = int(x[2:3])
        return row, col


#функция для ввода 'X':
def x_func():
    print('Введите номер клетки для крестика (Х) в формате "номер по вертикали:номер по горизонтали" (например, 1:2): ')
    row, col = data_control()

    if matrix_hello[row][col] == "-":
        matrix_hello[row][col] = "X"
        matrix_func()
    else:
        print("Данная клетка занята.")
        x_func()


#функция для ввода '0':
def y_func():
    print('Введите номер клетки для нолика (0) в формате "номер по вертикали:номер по горизонтали" (например, 1:2): ')
    row, col = data_control()

    if matrix_hello[row][col] == "-":
        matrix_hello[row][col] = "0"
        matrix_func()
    else:
        print("Данная клетка занята.")
        y_func()


matrix_hello_func()
matrix_func()


def data_since_func():
    if (matrix_hello[1][1] == matrix_hello[1][2] == matrix_hello[1][3]!='-'
        or matrix_hello[2][1] == matrix_hello[2][2] == matrix_hello[2][3] != "-"
        or matrix_hello[3][1] == matrix_hello[3][2] == matrix_hello[3][3] != "-"
        or matrix_hello[1][1] == matrix_hello[2][1] == matrix_hello[3][1] != "-"
        or matrix_hello[1][2] == matrix_hello[2][2] == matrix_hello[3][2] != "-"
        or matrix_hello[1][3] == matrix_hello[2][3] == matrix_hello[3][3] != "-"
        or matrix_hello[1][1] == matrix_hello[2][2] == matrix_hello[3][3] != "-"
        or matrix_hello[3][1] == matrix_hello[2][2] == matrix_hello[1][3] != "-"):
        return True
    else:
        return False


count = 0
for i in range((hello**2)-1):

    x_func()
    if data_since_func() == True:
        print('Выиграл крестик!')
        break

    if data_since_func() == False and count == 4:
        print('Ничья!')
        break

    y_func()
    if data_since_func() == True:
        print('Выиграл нолик!')
        break

    count += 1
