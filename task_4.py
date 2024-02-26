N = int(input())

forms = {}
for lines in range(N):
    words = input().split()
    forms[words[0]] = words[1:]

identify_object = input()

for form, objects in forms.items():
    if identify_object in objects:
        print(form)
