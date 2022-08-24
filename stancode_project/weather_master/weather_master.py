"""
File: weather_master.py
Name: Abbie Chen
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -1
def main():
	"""
	By inputting a sequence of numbers, that will end up in -100, Stan Code Weather 4,0 will conclude that:
	1. the highest temperature 2. the lowest temperature
	3. average temperature 4. how many days the weather will be lower than 16 degree
	"""
	print('StanCode \"Weather Master 4.0\"!')
	n = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if n == EXIT:
		# if no temperatures were entered
		print('No temperatures were entered.')
	else:
		maximum = n
		minimum = n
		x = 0
		y = 0
		sum = 0
		while True:
			sum += n
			y+= 1
			if n < 16:
				x+= 1
			n = int(input('Next Temperature: (or '+str(EXIT)+ ' to quit)? '))
			if n == EXIT:
				break
			if n > maximum:
				maximum = n
			if n < minimum:
				minimum = n


		print('Highest temperature: ' + str(maximum))
		print('Lowest temperature: ' + str(minimum))
		print('Average: '+str(sum/y))
		print(str(x)+' cold day(s)')




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
