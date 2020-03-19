"""
Created this to de-mystify the working of famous pattern_create and pattern_offset by MSF
Kudos to Svenito who has already done this job! (https://github.com/Svenito/exploit-pattern)
"""

import argparse
import string
import binascii

def main():

	parser = argparse.ArgumentParser(
		description='A tool to create and find cyclical patterns for buffer overflows.', 
		prog='buffpat.py',
		usage='%(prog)s --help <for help> -l <Length of pattern to create> -s <pattern to search>')
	parser.add_argument("-l", "--length", help="Length of the pattern", dest='length', type=int)
	parser.add_argument("-s", "--search", help="Pattern to search", type=str, dest='search')

	args = parser.parse_args()


	if args.length:
		create(args.length)
	if args.search:
		search(args.search)

def create(length):


	cyclic = ""

	for alp_u in string.ascii_uppercase:
		for alp_l in string.ascii_lowercase:
			for d in string.digits:
				if len(cyclic) <= length:
					cyclic += alp_u+alp_l+d

				
	final = cyclic[:length]
	print(final)
	

def search(find):
	
	if find.startswith("0x"):
		find = find.strip("0x")	

	to_search = binascii.unhexlify(find)
	to_search = to_search[::-1]

	sts = to_search.decode()
		
	data = ""

	for alp_u in string.ascii_uppercase:
		for alp_l in string.ascii_lowercase:
			for d in string.digits:
				data += alp_u+alp_l+d
				output = data.find(sts)
	if output > -1:
		print("The pattern was found at: "+output)
	else:
		print("[-] The pattern couldn't be found.")

	

if __name__ == '__main__':
	main()
