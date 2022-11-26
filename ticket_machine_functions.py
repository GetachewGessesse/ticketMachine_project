

def cosmetics():

    n1 = 1
    n2 = 0
    # line2 = 1
    while True:
        yield n1
        n1, n2 = n1 + 1, n2 + 1


wait = cosmetics()


def perfumery():
    n1 = 1
    n2 = 0
    # line2 = 1
    while True:
        yield n1
        n1, n2 = n1 + 1, n2 + 1


wait2 = perfumery()


def pharmaceutical():
    n1 = 1
    n2 = 0
    # line2 = 1
    while True:
        yield n1
        n1, n2 = n1 + 1, n2 + 1


wait3 = pharmaceutical()


def messages():
    c = wait
    d = wait2
    e = wait3
    print("Please wait and someone will assist you")
    print("******************************************")