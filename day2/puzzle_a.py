if __name__ == "__main__":
	errors = 0
	with open("./input.txt", "r") as f:
		for line in f:
			input_line = line.strip().split(" ")
			policy = input_line[0].split("-")
			occurrences = input_line[2].count(input_line[1][0])
			if int(policy[0]) <= occurrences <= int(policy[1]):
				errors += 1
	print(errors)