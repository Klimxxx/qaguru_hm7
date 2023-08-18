import zipfile
import os

file1_path = os.path.join('resources/docs-pytest-org-en-latest.pdf')
file2_path = os.path.join('resources/file_example_XLS_10.xls')
file3_path = os.path.join('resources/file_example_XLSX_50.xlsx')
file4_path = os.path.join('resources/new_csv.csv')
archive_name = 'tmp.zip'

with zipfile.ZipFile(archive_name, 'a') as zipf:
    zipf.write(file1_path, 'docs-pytest-org-en-latest.pdf')
    zipf.write(file2_path, 'file_example_XLS_10.xls')
    zipf.write(file3_path, 'file_example_XLSX_50.xlsx')
    zipf.write(file4_path, 'new_csv.csv')


    def test_zip():
        with zipfile.ZipFile(archive_name, 'r') as zipf:
            print(f'Содержимое архива: {zipf.namelist()}')
            assert zipf.namelist() == ['docs-pytest-org-en-latest.pdf', 'file_example_XLS_10.xls',
                                       'file_example_XLSX_50.xlsx', 'new_csv.csv']
            os.remove('tmp.zip')