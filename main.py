from stats import count_words

def get_book_text(filepath):
    try:
        with open(filepath) as b:
            file_text = b.read()
            return file_text
    except Exception:
        print("Filepath is invalid.")

def main():
    book_filepath = "./books/frankenstein.txt"
    wordcount = count_words(get_book_text(book_filepath))
    print(f"{wordcount} words found in the document")
    return

main()