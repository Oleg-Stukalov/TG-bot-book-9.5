

def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    ch = ',.!:;?'
    ssize = size
    if len(text) <= size + start:
        ssize = len(text) - start
    else:
        for i in range(size+start - 1, start, -1):
            if text[i] in ch and text[i+1] not in ch:
                break
            ssize -= 1
    return (text[start: start + ssize], ssize)


# Не удаляйте эти объекты - просто используйте
import os
import sys

BOOK_PATH = '../book/book.txt'
book: dict[int, str] = {}
PAGE_SIZE = 1050


# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> None:
    with open(path, 'rt', encoding='utf-8') as file:
        text = ''.join(file.readlines())

    page_num = 1  # key for book dict
    start = 0  # cursor position for _get_part_text()
    out = _get_part_text(text, start, PAGE_SIZE)
    while out[0] != '':
        book[page_num] = out[0].lstrip()
        page_num += 1
        start += out[1]
        out = _get_part_text(text, start, PAGE_SIZE)


# prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
# print(book)