words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
talk = set()
tmp = words[0][0]
n = 2
for i, word in enumerate(words):
    if word[0] != tmp or word in talk:
        a, b = divmod(i+1, n)
        a += 1
        if b == 0:
            a -= 1
            b = n
        print([b, a])
        break
    talk.add(word)
    tmp = word[-1]
else:
    print([0, 0])
