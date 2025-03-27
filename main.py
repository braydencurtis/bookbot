from stats import count_words
from stats import count_characters
from stats import sorted_list

book = "books/frankenstein.txt"

print(f"{count_words(book)} words found in the document")
print(count_characters(book))

print(sorted_list(count_characters(book)))