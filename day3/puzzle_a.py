if __name__ == "__main__":
	trees = 0
	with open("./input.txt", "r") as f:
		for i, line in enumerate(f):
			line = line.strip()
			trees += line[(i*3) % len(line)] == "#"
	print(trees)