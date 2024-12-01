def main():
    text = get_book_text("books/frankenstein.txt")
    words_amount = count_words(text)
    chars_dict = count_chars(text)
    print(chars_dict)

def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
