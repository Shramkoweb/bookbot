def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)


if __name__ == "__main__":
    main()
