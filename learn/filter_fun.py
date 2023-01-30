words = ['sky', 'cloud', 'wood', 'forest', 'tie', 'nice', 'cup']
filtered = filter(lambda e: len(e) == 3, words)
print(list(filtered))