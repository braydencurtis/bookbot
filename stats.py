def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(path_to_file):
    word_list = get_book_text(path_to_file).split()
    word_count = len(word_list)
    return word_count