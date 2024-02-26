N = int(input())

translation = {}
for pairs in range(N):
    pair = input().split()
    translation[pair[0]] = pair[1]

proposal = input().split()

for word in proposal:
    if word in translation:
        number = proposal.index(word)
        proposal[number] = translation[word]

for word in proposal:
    print(word, end=' ')
    