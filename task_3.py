N = int(input())

antonyms = {}
for pairs in range(N):
    pair = input().split()
    antonyms[pair[0]] = pair[1]

word = input()

if word not in antonyms and word not in antonyms.values():
    print(word)
else:
    for antonyms_1, antonyms_2 in antonyms.items():
        if antonyms_1 == word:
            print(antonyms_2)
        if antonyms_2 == word:
            print(antonyms_1)
