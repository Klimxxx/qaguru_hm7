import pypdf, os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь
file_path = os.path.join('resources/docs-pytest-org-en-latest.pdf')


def test_pdf1():
    reader = pypdf.PdfReader(file_path)
    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    text = first_page.extract_text()
    print("Общее количество страниц: ", number_of_pages)
    assert number_of_pages == 412
    print("На странице отображено: ", first_page)
    print("Текст на данной страницы: ", text)

    count = 0
    for image_file in first_page.images:
        with open(str(count) + image_file.name, 'wb') as fp:
            fp.write(image_file.data)
            count += 1
    assert count == 1
