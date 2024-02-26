words = input().split()

answer = {}
for word in words:
    if word in answer:
        answer[word] += 1
    else:
        answer[word] = 1

answer = sorted(answer.items(), key=lambda item: item[1], reverse=True)
for word in answer:
    print(word[0])