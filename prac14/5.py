def count_descendants(tree, person):
    total = 0
    if person in tree:
        for child in tree[person]:
            total += 1 + count_descendants(tree, child)
    return total

n = int(input())

tree = {}

for _ in range(n):
    parent, child = input().split()
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

name = input()

print(count_descendants(tree, name))