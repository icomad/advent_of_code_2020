import math

def count_trees(right, down):
	trees = 0
	spot = 0
	with open("./input.txt", "r") as f:
		for i, line in enumerate(f):
			if i % down != 0:
				continue
			line = line.strip()
			trees += line[spot % len(line)] == "#"
			spot += right
	return trees

if __name__ == "__main__":
	slopes = [count_trees(1, 1), count_trees(3, 1), count_trees(5, 1), count_trees(7, 1), count_trees(1, 2)]
	print(math.prod(slopes))