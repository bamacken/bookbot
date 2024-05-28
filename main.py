def main():
    print("--- Begin report of books/frankenstein.txt ---")
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = character_count(text)
    chars_dict = character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    print(f"{num_words} words found in the document\n")
    for entry in chars_sorted_list:
        char = entry["char"]
        num = entry["num"]
        print(f"The {char} character was found {num} times")
    print(f"The {char} character was found {chars_dict[char]} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def character_count(text):
    characters = {}
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in characters:
                characters[lower_char] += 1
            else:
                characters[lower_char] = 1
    return characters


main()

