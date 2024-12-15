from typing import List, Dict
from collections import Counter

REPORT_HEADER = "--- Begin report of {} ---"
REPORT_FOOTER = "--- End report ---"
WORD_COUNT_MESSAGE = "{} words found in the document\n"
CHAR_COUNT_MESSAGE = "The '{}' character was found {} times"

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_amount = count_words(text)
    chars_dict = count_chars(text)
    result = chars_dict_to_sorted(chars_dict)

    print(REPORT_HEADER.format(book_path))
    print(WORD_COUNT_MESSAGE.format(words_amount))

    for item in result:
        if not item['char'].isalpha():
            continue
        print(CHAR_COUNT_MESSAGE.format(item['char'], item['num']))

    print(REPORT_FOOTER)


def chars_dict_to_sorted(chars_dict: Dict[str, int]) -> List[Dict[str, int]]:
    result = []
    for char, value in chars_dict.items():
        result.append({"char": char, "num": value})
    result.sort(reverse=True, key=sort_chars)
    return result


def sort_chars(d: Dict[str, int]) -> int:
    return d['num']


def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> Dict[str, int]:
    return Counter(text.lower())


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
