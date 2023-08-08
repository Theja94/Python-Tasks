"""Given an input string, write a function that returns the run
length encoded string for the input string.
For Example:
Input: wwwwaaadebbbbbw
Output: w4a3d1e1b5w1
"""


def run_len_enc(strng):
	n = len(strng)
	i = 0
	while i < n:
		count = 1
		while (i < n - 1 and strng[i] == strng[i + 1]):
			count += 1
			i += 1
		i += 1

		print(strng[i - 1] + str(count), end = "")


if __name__ == "__main__":
	st = "wwwwaaadebbbbbw"
	run_len_enc(st)
