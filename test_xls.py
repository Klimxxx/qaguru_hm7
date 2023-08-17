import xlrd, os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь
file_path = os.path.join('resources/file_example_XLS_10.xls')


def test_xls():
    book = xlrd.open_workbook(file_path)

    print(f'Количество листов {book.nsheets}')
    assert book.nsheets == 1
    print(f'Имена листов {book.sheet_names()}')
    assert book.sheet_names() == ['Sheet1']
    sheet = book.sheet_by_index(0)
    print(f'Количество колонок  {sheet.ncols}')
    assert sheet.ncols == 8
    print(f'Количество строк    {sheet.nrows}')
    assert sheet.nrows == 10
    print(f'Пересечение строки и столбца {sheet.cell_value(rowx=3, colx=2)}')
    for rx in range(sheet.nrows):
        print(sheet.row(rx))
    assert rx == 9
