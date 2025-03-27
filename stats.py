from collections import Counter

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(path_to_file):
    word_list = get_book_text(path_to_file).split()
    word_count = len(word_list)
    return word_count

def count_characters(path_to_file):
    lower_case_contents = get_book_text(path_to_file).lower()
    char_counts = Counter(lower_case_contents)
    return char_counts

def sorted_dict(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    sorted_dictionary = dict(sorted_items)
    return sorted_dictionary