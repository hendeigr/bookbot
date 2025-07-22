from stats import get_num_words
from stats import get_char_count
from stats import sorted_char_count

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------""")
    text = get_book_text(sys.argv[1])
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    s = sorted_char_count(get_char_count(text))
    for l in s:
        if l['char'].isalpha():
            print(l["char"] + ": " + str(l["num"]))
    print("============= END ===============")
main()
