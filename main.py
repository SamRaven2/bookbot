from stats import *
import sys

def get_book_text(filepath):
    try:
        with open(filepath) as b:
            file_text = b.read()
            return file_text
    except Exception:
        print("Filepath is invalid.")

def print_report(file_path, word_count, sorted_letter_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for set in sorted_letter_list:
        if set["char"].isalpha():
            print(f"{set["char"]}: {set["num"]}")
    print("============= END ===============")
    return

def main():
    arguments = sys.argv

    if len(arguments) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_filepath = arguments[1]
    book_text = get_book_text(book_filepath)
    wordcount = count_words(book_text)
    sorted_lettercounts = sort_dict(count_letters(book_text))

    print_report(book_filepath, wordcount, sorted_lettercounts)
    
    return

main()