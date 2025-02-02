import logging
import sys
import time
from time import gmtime, strftime

def main():
	# Configure the logging system
	logging.basicConfig(filename ='/opt/results/app-log3.txt', level = logging.INFO)
	
	# Variables (to make the calls that follow work)
	hostname = 'www.python.org'
	item = 'spam'
	filename = 'data.csv'
	mode = 'r'
	for i in range(15):
		time.sleep(6)
		# Example logging calls (insert into your program)
		print("hello world git reference - {}".format(i))
		logging.info("hello world git reference master branch - {}".format(i))
		logging.info(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

if __name__ == '__main__':
	main()
sys.exit
