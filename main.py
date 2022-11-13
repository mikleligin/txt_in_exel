import pandas
import openpyxl
import time


def read_word(name_of_file):
    file = open(name_of_file, encoding='utf-8', mode='r')
    all_text = []
    while True:
        x = file.readline()
        if not x:
            break
        print(x)
        all_text.append(x.replace('\n', ''))
    clear = list(filter(None, all_text))
    file.close()
    return clear


def in_exel(list_of_elements):
    exel = openpyxl.Workbook()
    exel.save('table.xlsx')
    df = pandas.DataFrame(list_of_elements)
    df.to_excel('table.xlsx')
    print(df)


if __name__ == '__main__':
    # name = '2.txt'
    name = input('Введите название файла ')
    start = time.time()
    clear_txt = read_word(name)
    print(clear_txt)
    in_exel(clear_txt)
    end = time.time()
    print(end-start)
