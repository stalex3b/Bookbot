from pathlib import Path
import re

BOOK_PATH = Path('book/book_utf.txt')
PAGE_SIZE = 950

book: dict[int, str] = {}


def _get_part_text(text: str, start: int = 0, page_size: int = 1000) -> tuple[str, int]:
    fin: int = start + page_size
    part_text: str = text[start: fin].lstrip('.')
    if text[fin:fin + 1] == '.':
        part_text = part_text.strip(',.!:;?')
    page = re.sub(r'[^,\.!:;?]*?$', '', part_text)
    return page, len(page)


def prepare_book(path: Path) -> None:
    with open(path, encoding='utf-8-sig') as f:
        text = f.read()
    num_page = 0
    while True:
        page, shift = _get_part_text(text, 0, PAGE_SIZE)
        if page:
            num_page += 1
            book[num_page] = page.strip()
            text = text[shift:]
        else:
            break


abs_path = Path.cwd().joinpath(BOOK_PATH)
prepare_book(abs_path)
