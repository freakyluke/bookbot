import sys
from stats import word_count
from stats import char_count
from stats import sort_count
def get_book_text(fp):
    with open(fp) as f:
        fc =f.read()
    return fc


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(f"Found {word_count(get_book_text(sys.argv[1]))} total words")
    sorted = sort_count(char_count(get_book_text(sys.argv[1])))
   

    for sorte in sorted:
        print (f"{sorte["char"]}: {sorte["num"]}")


main()