if __name__ == "__main__":
	valid_pwds = 0
	with open("./input.txt", "r") as f:
		for line in f:
			input_line = line.strip().split(" ")
			policy = input_line[0].split("-")
			occurrences = [p+1 for p,c in enumerate(input_line[2]) if c == input_line[1][0]]
			if (int(policy[0]) in occurrences) != (int(policy[1]) in occurrences):
				valid_pwds += 1
	print(valid_pwds)