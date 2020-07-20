verse = ("If you can keep your head when all about you\n"
        "Are losing theirs and blaming it on you,\n"
        "If you can trust yourself when all men doubt you,\n"
        "But make allowance for their doubting too;\n"
        "If you can wait and not be tired by waiting,\n"
        "Or being lied about, don’t deal in lies,\n"
        "Or being hated, don’t give way to hating,\n"
        "And yet don’t look too good, nor talk too wise:")

print(verse)
print()
print("Length of the string variable verse: {}".format(len(verse)))
print("Index of the first occurrence of the word 'and' in verse: {}".format(verse.find('and')))
print("Index of the last occurrence of the word 'you' in verse: {}".format(verse.rfind('you')))
print("Count of occurrences of the word 'you' in the verse: {}".format(verse.count('you')))
