import re

def find_max_length_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = re.findall(r'\b\w+\b', text)
    max_length = max(len(word) for word in words)
    max_length_words = [word for word in words if len(word) == max_length]
    return max_length_words


max_length_words = find_max_length_word("example.txt")
for word in max_length_words:
    print(word)
