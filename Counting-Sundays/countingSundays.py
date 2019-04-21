# File Name: countingSundays.py
# Author: Esther Heralta Espinosa
# Date: 04/20/19
# Description of the program: You are given the following information, but you may prefer to do some research for yourself.
#
#							                1 Jan 1900 was a Monday.
#							                Thirty days has September,
#							                April, June and November.
#							                All the rest have thirty-one,
#							                Saving February alone,
#							                Which has twenty-eight, rain or shine.
#							                And on leap years, twenty-nine.
#							                A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#             
#							                How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?		

from datetime import date

def main():

	countSunday = 0 #number of Sundays between 1 Jan 1901 and 31 Dec 2000

	for year in range (1901, 2001): #from 1901 to 2000
		for month in range (1, 13): #from 1 to 12
			day = date(year, month, 1)
			dayOfWeek = day.weekday()
			if (dayOfWeek == 6): #6 == Sunday
					countSunday += 1

	print("\nThere are {0} Sundays that fell on the first of the month during Jan 1st, 1901 and Dec 31, 2000. \n".format(countSunday))

if __name__ == "__main__":
	main()	
