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


def sort_on(dict):
    return dict["num"]

def sorted_list(list):
    sorted = list.sort(reverse=True, key=sort_on)
    print(sorted)

