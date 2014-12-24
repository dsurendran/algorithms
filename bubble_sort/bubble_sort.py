import random


def bubble_sort(inp):
    for i in range(len(inp)):
        for j in range(i, len(inp)):
            if inp[i] > inp[j]:
                inp[i], inp[j] = inp[j], inp[i]


if __name__ == '__main__':
    inp = random.sample(range(100), 50)
    print(inp)
    bubble_sort(inp)
    print(inp)