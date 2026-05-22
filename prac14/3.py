n = int(input())

dictionary = {}

for _ in range(n):
    antonym1, antonym2 = input().split()
    dictionary[antonym1] = antonym2
    dictionary[antonym2] = antonym1

word = input()
if word in dictionary:
    print(dictionary[word])
else:
    print(word)
