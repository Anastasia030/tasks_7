n = int(input())

translation = {}
for pairs in range(n):
    eng, ru = input().split()
    translation[eng] = ru


for word in input().split():
    print(translation.get(word, word), end=' ')

'''
for word in proposal:
    if word in translation:
        number = proposal.index(word)
        proposal[number] = translation[word]

for word in proposal:
    print(word, end=' ')
'''