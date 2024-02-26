N = int(input())

descendants = {}
descendant = []
for pairs_names in range(N):
    pair_name = input().split()
    if pair_name[0] not in descendants:
        descendant = [pair_name[1]]
    else:
        descendant.append(pair_name[1])
    descendants[pair_name[0]] = descendant


def count_descendants(search_name):
    count = 0
    if search_name not in descendants:
        return 0
    for name, sons in descendants.items():
        if name == search_name:
            count += len(sons)
            while sons:
                count += count_descendants(sons[0])
                sons = sons[1:]
    return count


given_name = input()
print(count_descendants(given_name))
