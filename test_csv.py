import csv, os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь
file_path = os.path.join('resources/new_csv.csv')


def test_csv1():
    with open(file_path, 'w') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        assert csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        assert csvwriter.writerow(['Alex', 'Serj', 'Yana'])

def test_csv2():
    with open(file_path) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        for row in csvreader:
            print(row)
        assert row == ['Alex', 'Serj', 'Yana']