from stats import get_num_words, character_count

def get_book_text(file_path):
    file_content = None
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    file_path = './books/frankenstein.txt'
    file_content = get_book_text(file_path)

    num_words = get_num_words(file_content)

    char_dict = character_count(file_content)

    print(f'Found {num_words} total words')

    print(char_dict)

if __name__ == "__main__":
    main()