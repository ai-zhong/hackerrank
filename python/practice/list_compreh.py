wordlist = ['cat', 'dog', 'rabbit']
# method 1: list comprehension, unpack list inside list:
# [x for l in list for x in l]
ans = [aletter for aword in wordlist for aletter in aword]
print(list(set(ans)))

# method 2:
print([ch for ch in ''.join(wordlist)])

# method 3:
print([word[i] for word in wordlist for i in range(len(word))])
