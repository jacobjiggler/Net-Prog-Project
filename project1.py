import sys

if __name__ == '__main__':
	with open('routes.txt') as r:
		content = r.readlines()
	print(content)


	dict = {}
	with open('arp.txt') as arp:
		for line in arp:
			dict[line.split(" ")[0]] = line.split(" ")[1]
