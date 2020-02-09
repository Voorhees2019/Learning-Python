import itertools as it

pin = [7, 5, 2, 8]
print(list(it.permutations(pin)))

# колода карт
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S']  # масть
lst = list(it.product(ranks, suits))
print(lst)

print(list(it.combinations(lst, 2)))  # all possible combinations to pull two cards out from this card deck
print(list(it.combinations('ABCD', 2)))

