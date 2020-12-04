import re

if __name__ == "__main__":
	fields = ['eyr', 'hgt', 'hcl', 'pid', 'byr', 'ecl', 'iyr']
	valid = 0
	with open("./input.txt", "r") as f:
		passports = [line.replace('\n', ' ') for line in f.read().split("\n\n") if line]
		for passport in passports:
			valid += all(field in passport for field in fields)
	print(valid)