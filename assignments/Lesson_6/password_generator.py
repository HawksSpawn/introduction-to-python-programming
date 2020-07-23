from random import choice

word_file = "words.txt"
word_list = []

with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

def generate_password():
    """Return a string consisting of three random words concatenated together without spaces."""
    
    password = [choice(word_list) for i in range(3)]
    return ("").join(password)

print(generate_password())
