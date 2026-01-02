def get_num_words(file):
    file_list = file.split()
    count_of_words = len(file_list)
    return count_of_words

def character_count(file_text):
    char_dict = {}
    for t in file_text:
        if t.lower() in char_dict:
            char_dict[t.lower()] += 1
        else:
            char_dict[t.lower()] = 1
    return char_dict