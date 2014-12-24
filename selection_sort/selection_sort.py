import random


def selection_sort(input):
    for i in range(len(input)):
        for j in range(i, len(input)):
            if input[i] > input[j]:
                input[i], input[j] = input[j], input[i]
    return input


if __name__ == '__main__':
    input_list = sorted(random.sample(range(1000), 50))
    print(selection_sort(input_list))