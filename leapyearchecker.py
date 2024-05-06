def check_year():
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		print(str(year) + " is a leap year.")
	else:
		print(str(year) + " is not leap year.")
year = int(input("enter year:"))
check_year()