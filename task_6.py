N = int(input())
M = int(input())

pairs_cities = []
number_citi = {}
numbers = list(range(N+1))


def list_to_matrix(cities):
    ways = []
    for citi in range(N):
        ways.append([float('inf')]*N)
    for town, town_2, distance in cities:
        ways[town][town_2] = int(distance)
        ways[town_2][town] = int(distance)
    return ways


def floyd(ways):
    for citi in range(N):
        for column in range(N):
            for row in range(N):
                ways[column][row] = min(ways[column][row], ways[column][citi]+ways[citi][row])
    return ways


for pair_cities in range(M):
    pair = input().split()

    if pair[0] in number_citi:
        pair[0] = number_citi[pair[0]]
    else:
        number_citi[pair[0]] = numbers[0]
        pair[0] = numbers[0]
        numbers = numbers[1:]

    if pair[1] in number_citi:
        pair[1] = number_citi[pair[1]]
    else:
        number_citi[pair[1]] = numbers[0]
        pair[1] = numbers[0]
        numbers = numbers[1:]

    pairs_cities.append(tuple(pair_cities for pair_cities in pair))


matrix_distance = list_to_matrix(pairs_cities)
minimal_distance = floyd(matrix_distance)

given_citi_1, given_citi_2 = input().split()

given_citi_1 = number_citi[given_citi_1]
given_citi_2 = number_citi[given_citi_2]

for citi_1 in range(N):
    for citi_2 in range(N):
        if citi_1 == given_citi_1 and citi_2 == given_citi_2:
            print(minimal_distance[citi_1][citi_2])
