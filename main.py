def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = character_count(text)
    print(chars_dict)

def character_count(text):
    letter_count ={}
    for char in text:
        lowered = char.lower()
        if lowered in letter_count and lowered.isalpha():
            letter_count[lowered] += 1
        elif lowered.isalpha():
            letter_count[lowered] = 1   
    return letter_count
  
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
         return f.read()


if __name__ == "__main__":
    main()