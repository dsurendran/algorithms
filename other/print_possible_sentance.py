arr = [["you", "we", "aaa"],
       ["have", "are", "bbb"],
       ["sleep", "eat", "drink"]]


def func(arr, curr_str, index, n):
    if index == n:
        print curr_str
    else:
        for str in arr[index]:
            temp = curr_str
            curr_str = curr_str + " " + str
            func(arr, curr_str, index + 1, n)
            curr_str = temp


def print_util(arr):
    curr_str = ""
    index = 0
    n = 3
    func(arr, curr_str, index, n)


print_util(arr)
