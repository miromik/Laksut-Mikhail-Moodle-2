import random

koodi1 = (
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9)
)

koodi2 = (
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9)
)

print("Kolminumeroinen koodi:", *koodi1)
print("Nelinumeroinen koodi:", *koodi2)