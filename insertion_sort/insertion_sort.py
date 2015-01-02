import random


def insertion_sort(inp):
	for i in range(1,len(inp)):
		key = inp[i]
		j = i - 1
		while j >= 0 and inp[j] > key:
			inp[j+1] = inp[j]
			j = j - 1
		inp[j+1] = key
	return inp

if __name__ == '__main__':
    inp = random.sample(range(100), 50)
    print(inp)
    insertion_sort(inp)
    print(inp)
