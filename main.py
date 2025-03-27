from stats import count_words
from stats import count_characters
from stats import sorted_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book}...")
print("----------- Word Count ----------")
print(f"Found {count_words(book)} total words")
print("--------- Character Count -------")

for i in sorted_dict(count_characters(book)):
    if i.isalpha() == True: 
        print(f"{i}: {sorted_dict(count_characters(book))[i]}")
        
print("============= END ===============")



