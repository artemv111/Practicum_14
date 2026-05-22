n = int(input())

dictionary = {}

for _ in range(n):
    words = input().split()
    form = words[0]
    objects = words[1:]

    for object in objects:
        dictionary[object] = form

item = input()
if item in dictionary:
    print(dictionary[item])
else:
    print(item)