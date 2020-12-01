import math

def find_subset_sum(arr, total):
    i = 0
    j = len(arr) - 1
    while i<j:
        head = arr[i]
        tail = arr[j]
        if head + tail == total:
            return [head, tail]
        elif head + tail < total:
            i += 1
        else:
            j -= 1
    return []

if __name__ == "__main__":
	with open("./input") as f:
		expenses = sorted([int(line.strip()) for line in f])
		out = find_subset_sum(expenses, 2020)
		print(math.prod(out))
