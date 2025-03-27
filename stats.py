from collections import Counter

# Convert book.txt file into a workable string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# count the number of words in the book file and return an Int
def count_words(path_to_file):
    word_list = get_book_text(path_to_file).split()
    word_count = len(word_list)
    return word_count

# count the number of characters in the book file, and return a dictionary
def count_characters(path_to_file):
    lower_case_contents = get_book_text(path_to_file).lower()
    char_counts = Counter(lower_case_contents)
    return char_counts

# sort the dictionary by value in descending order
def sorted_dict(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    sorted_dictionary = dict(sorted_items)
    return sorted_dictionary