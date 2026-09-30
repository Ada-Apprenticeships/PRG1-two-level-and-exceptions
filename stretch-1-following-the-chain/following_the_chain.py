"""
Optional stretch. A two-level structure where the second row is not
data about the first, but directions to the next item.

Row 0 holds plant names in the order they were planted.
Row 1 holds, for each plant, the position of the next one
alphabetically. None means there is no next one.
"""

plants = [
    ["Begonia", "Daisy", "Lily", "Peony", "Rose", "Sunflower", "Lavender"],
    [1, 6, 3, 4, 5, None, 2],
]

current = 0
alphabetical = []

while current is not None:
    alphabetical.append(plants[0][current])
    current = plants[1][current]

print(" -> ".join(alphabetical))
