def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    
    char_count = get_char_count(text)
    
    list_of_letters = get_list_of_letters(char_count)
    list_of_letters.sort(reverse=True, key=sort_on_num)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for letter in list_of_letters:
        print(f"The '{letter["char"]}' character was found {letter["num"]}")
    print("--- End report ---")
    #print(f"{num_words} words found in the document")
    #print(f"The Breakdown looks like this:")
    #print(f"{char_count}")
    #print(f"{list_of_letters}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    counts = {}
    for char in text:
        lowered = char.lower()
        if lowered in counts:
            counts[lowered] += 1
        else:
            counts[lowered] = 1
    return counts

def sort_on_num(dict):
    return dict["num"]

def get_list_of_letters(dict):
    l = []
    for char in dict:
        if char.isalpha():
            entry = {}
            entry["char"] = char
            entry["num"] = dict[char]
            l.append(entry)
    return l

main()