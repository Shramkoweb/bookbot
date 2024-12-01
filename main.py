def main():
    text = get_book_text("books/frankenstein.txt")
    words_amount = count_words(text)
    print(f"{words_amount} words found in the document")

def count_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
