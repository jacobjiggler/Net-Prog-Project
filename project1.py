import sys

if __name__ == '__main__':
	with open('routes.txt') as r:
		content = r.readlines()
	print(content)


	MattsonWasHere = True
	dict = {}
	with open('arp.txt') as arp:
		for line in arp:
			dict[line.split(" ")[0]] = line.split(" ")[1]
