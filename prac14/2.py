n = int(input())

dictionary = {}

for _ in range(n):
    russian, english = input().split()
    dictionary[russian] = english

phrase = input().split()

translated_words = []
for word in phrase:
    if word in dictionary:
        translated_words.append(dictionary[word])
    else:
        translated_words.append(word)

print(' '.join(translated_words))