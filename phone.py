def load_file_csv(file_my, sep=';', end='\n'):
    ''' Загружаем файл csv ввиде списка '''
    with open(file_my, 'r', encoding='utf-8') as f:
        s = [i.replace(end,'').split(sep) for i in f]
    return s

def print_csv(spr_csv):
    ''' Выводим на экран файл csv ввиде списка '''
    print('\033c', end='')
    max_spr = max_csv(spr_csv)
    hyphen = sum(max_spr) + len(max_spr) * 3 + 6
    print('-' * hyphen)
    for row in spr_csv:
        if spr_csv.index(row) == 0:
            print(f'|  № |', end='')
        else:
            print(f'|{spr_csv.index(row):3} |', end='')
        for q in range(len(row)):
            print(f' {row[q]:{max_spr[q]}} |', end='')
        print()
        if spr_csv.index(row) == 0:
            print('-' * hyphen)        
    print('-' * hyphen)
    return

def max_csv(spr_csv):
    ''' Вычисляем в списке csv максимальные длины в столбцах '''
    d = [len(s) for s in spr_csv[0]]
    for row in spr_csv:
        for q in range(len(row)):
            if d[q] < len(row[q]):
                d[q] = len(row[q])
    return d

def add_line(spr_csv):
    ''' Добавляем новую строку в список '''
    return [[input(f'Введите \'{spr_csv[0][i]}\': ') for i in range(len(spr_csv[0]))]]


def del_line(spr_csv):
    ''' Удаляем строку из списка '''
    print_csv(spr_csv)
    line_del = int(input('Введите, какую удалить строку: '))
    if 0 < line_del < len(spr_csv):
        del spr_csv[line_del]
    else:
        print('Нельзя удалить')
    return


def rename(spr_csv, col):
    print_csv(spr_csv)
    line_ren = int(input('Введите, какую изменить строку: '))
    if 0 < line_ren < len(spr_csv):
        spr_csv[line_ren][col] = input(f'Введите \'{spr_csv[0][col]}\' вместо {spr_csv[line_ren][col]}: ')
    else:
        print('Нельзя изменить строку')
    return

def save_file_csv(file_my, spr_csv, sep=';', end='\n'):
    txt =''
    for i in spr_csv:
        for j in i:
            txt += j + sep
        txt = txt[:-1] + end 
    with open(file_my, 'w', encoding='utf-8') as f:
        f.write(txt)
    return

def print_menu():
    print()
    for key in menu_options.keys():
        print(key, '>', menu_options[key])

menu_options = {
    1: 'Добавить строку',
    2: 'Удалить строку\n',
    3: f'Изменить \'{spr[0][0]}\' в строке',
    4: f'Изменить \'{spr[0][1]}\' в строке',
    5: f'Изменить \'{spr[0][2]}\' в строке',
    6: f'Изменить \'{spr[0][3]}\' в строке\n',
    7: 'Вывести на экран список',
    8: 'Загрузить файл в список',
    9: 'Записать список в файл',
    0: 'Выход',
}

if __name__ == '__main__':
    while (True):
        file_phone = 'phone.csv'
        spr = load_file_csv(file_phone)
        print_csv(spr)
        print_menu()
        option = ''
        try:
            option = int(input('Введите команду: '))
        except:
            print('Ошибка ввода, повторите ввод ...')
        if option == 1:
            spr += add_line(spr)
            save_file_csv(file_phone, spr)
            print('\033c', end='')
            print_csv(spr)
        elif option == 2:
            del_line(spr)
            save_file_csv(file_phone, spr)
            print('\033c', end='')
            print_csv(spr)
        elif option == 3:
            rename(spr, 0)
            save_file_csv(file_phone, spr)
            print_csv(spr)
        elif option == 4:
            rename(spr, 1)
            save_file_csv(file_phone, spr)
            print_csv(spr)            
        elif option == 5:
            rename(spr, 2)
            save_file_csv(file_phone, spr)
            print_csv(spr)            
        elif option == 6:
            rename(spr, 3)
            save_file_csv(file_phone, spr)
            print_csv(spr)            
        elif option == 7:
            print_csv(spr)
        elif option == 8:
            spr = load_file_csv(file_phone)
            print_csv(spr)
        elif option == 9:
            save_file_csv(file_phone, spr)
            print_csv(spr)
        elif option == 0:
            print('Всего хорошего')
            exit()
        else:
            print('Ошибка ввода, такой команды нет, повторите ввод ...')
