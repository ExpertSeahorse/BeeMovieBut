import string


def bee(buzz):
    """
    Takes a string and replaces all instances of a word with the entire string
    "The bee movie script, but every time they say bee it is replaced with the entire bee movie script"
    :param buzz:
    :return:
    """
    d = buzz.split()
    c = []
    q = 'bee'
    p = 'Bee'
    for i in d:
        if q in i:
            i = buzz
            c.append(i)
        elif p in i:
            i = buzz
            c.append(i)
        else:
            c.append(i)
    return " ".join(c)


def stats(s):
    caps = 0
    lower = 0
    xa = 0
    xe = 0
    xi = 0
    xo = 0
    xu = 0
    for i in s:
        if i in string.ascii_uppercase:
            caps += 1
        elif i in string.ascii_lowercase:
            lower += 1

        if i in "Aa":
            xa += 1
        elif i in "Ee":
            xe += 1
        elif i in "Ii":
            xi += 1
        elif i in "Oo":
            xo += 1
        elif i in "Uu":
            xu += 1

        else:
            lower += 1
    print("The number of uppercase letters: ", caps)
    print("The number of lowercase letters: ", lower)
    print("The number of As: ", xa)
    print("The number of Es: ", xe)
    print("The number of Is: ", xi)
    print("The number of Os: ", xo)
    print("The number of Us: ", xu)


# Reads the input file
with open('input.txt') as j:
    read = j.read()

# enables the output file to be written to
with open('output.txt', 'w') as k:
    k.write(bee(read))
# fly = str(input("You know what to do"))           For terminal inputs

print("Stats before:")
stats(read)
print("\n\nStats after: ")
stats(bee(read))
