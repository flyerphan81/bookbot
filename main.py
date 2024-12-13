def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = character_count(text)
    print(chars_dict)

def character_count(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz.!?(),"\'-:;1234567890[]@#*_&/%$'
    letter_count ={}
    words = text.split()
    for char in alphabet:
       letter_count[char] = 0
    
    for word in words:
        lower_string = word.lower()
        for char in lower_string:
            letter_count[char] += 1
    return letter_count
  
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
         return f.read()


if __name__ == "__main__":
    main()