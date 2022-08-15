"""
File: largest_digit.py
Name: Abbie Chen
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int
	:return: int
	"""
	max_v = 0
	return find_largest_digit_helper(n, max_v)


def find_largest_digit_helper(n, max_v):
	if n == 0:
		return max_v
	else:
		if n > 0:
			if n % 10 > max_v:
				max_v = n % 10
			n = n // 10
		else:
			n = n * -1
		return find_largest_digit_helper(n, max_v)


if __name__ == '__main__':
	main()
