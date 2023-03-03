import random
import sys


def gendyck(n):

    if n == 0:
        return ""

    brackets = ['round', 'square', 'curved']
    b = random.choice(brackets)

    if b == "round":
        b0 = '('
        b1 = ")"    

    elif b == "square":
        b0 = "["
        b1 = "]"

    elif b == "curved":
        b0 = "{"
        b1 = "}"

    byte = random.choice([0, 1])

    if byte:
        # dyck string of size 1 + size1 + size2
        # size1 + size2 = n - 1
        s1 = random.randint(0, n-1)
        s2 = n - 1 - s1
        return b0 + gendyck(s1) + b1 + gendyck(s2)
    else:
        # dyck string of size 2 + size
        return b0 + gendyck(n-1) + b1  


if __name__ == "__main__":

    d = gendyck(int(sys.argv[1]))
    print(d)




