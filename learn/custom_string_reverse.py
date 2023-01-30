def reversed_string(word):
    rev = ''
    n = len(word)
    while n > 0:
        n -= 1
        rev += word[n]
    return rev

word = 'forest'
print(reversed_string('forest'))