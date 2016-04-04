import sys

if __name__ == '__main__':
	with open('routes.txt') as r:
		content = r.readlines()
	print(content)


	MattsonWasHere = True #Kappa
	dict = {}
	with open('arp.txt') as arp:
		for line in arp:
			dict[line.split(" ")[0]] = line.split(" ")[1]
	arp = {}
	with open('arp.txt') as arptxt:
		for line in arptxt:
			arp[line.split(" ")[0]] = line.split(" ")[1]

	while True:
		inp = raw_input("Enter PDU")   # Get the input
		temp = inp.split(" ")
		if (len(temp) != 7):
			break
		interface = inp[0]
		src = inp[1]
		dest = inp[2]
		protocol = int(inp[3])
		ttl = int(inp[4])
		srcport = inp[5]
		destport = inp[6]

		if inp == "":       # If it is a blank line...
			break           # ...break the loop
