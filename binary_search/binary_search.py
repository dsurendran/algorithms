import random


def binary_search(input_list, value):
    if input_list is None:
        return False
    mid = len(input_list) // 2
    if len(input_list) == 1:
        return value == input_list[0]
    if input_list[mid] == value:
        return True
    elif value < input_list[mid]:
        return binary_search(input_list[:mid], value)
    elif value > input_list[mid]:
        return binary_search(input_list[mid:], value)
    return False


if __name__ == '__main__':
    input_list = sorted(random.sample(range(1000), 500))
    print(binary_search(input_list, 100))
    print(binary_search(input_list, 10000))
    print(binary_search(input_list, 500))
