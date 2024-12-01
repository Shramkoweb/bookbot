def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_amount = count_words(text)
    chars_dict = count_chars(text)
    result = chars_dict_to_sorted(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words_amount} words found in the document\n")

    for item in result:
        if not item['char'].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def chars_dict_to_sorted(chars_dict):
    result = []
    for char, value in chars_dict.items():
        result.append({"char": char, "num": value})
    result.sort(reverse=True, key=sort_chars)
    return result


def sort_chars(d):
    return d['num']


def count_words(text):
    return len(text.split())


def count_chars(text):
    chars = {}
    for c in text.lower():
        chars[c] = chars.get(c, 0) + 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
