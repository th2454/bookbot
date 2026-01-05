from stats import get_num_words, character_count, chars_dict_to_sorted_list
import sys

def get_book_text(file_path):
    file_content = None
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def pretty_report(num_words, sorted_dict, file_path):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for dict in sorted_dict:
        if dict['char'].isalpha():
            print(f'{dict['char']}: {dict['num']}')
    print('============= END ===============')

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    file_path = sys.argv[1]
    file_content = get_book_text(file_path)

    num_words = get_num_words(file_content)

    char_dict = character_count(file_content)

    sorted_dict = chars_dict_to_sorted_list(char_dict)

    pretty_report(num_words, sorted_dict, file_path)

if __name__ == "__main__":
    main()