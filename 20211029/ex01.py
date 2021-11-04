str = "The Espresso Spirit"
print(str.upper())
print(str.lower())
print(str)


def birth_only(birth):
    return birth[:6]
# alt +enter

a = birth_only("070609-2011xxx")
print(a)

a = birth_only("090716-1012xxx")
print(a)

