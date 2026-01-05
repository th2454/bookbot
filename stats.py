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

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})

    sorted_list.sort(reverse=True, key=sort_on) 
    
    return sorted_list