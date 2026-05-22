words = input().split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

for i in range(len(unique_words)):
    for j in range(i + 1, len(unique_words)):
        if frequency[unique_words[i]] < frequency[unique_words[j]]:
            unique_words[i], unique_words[j] = unique_words[j], unique_words[i]

for word in unique_words:
    print(word)