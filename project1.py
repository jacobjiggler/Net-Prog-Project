import sys

class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.destination = None
        self.gateway = None
        self.interface = None

if __name__ == '__main__':
    with open('routes.txt') as r:
        routeslines = r.readlines()

    routes = []
    routesbinary = []
    for line in routeslines:
        routes.append(line.split())

    root = Node()
    cNode = root
    temp = []
    for val in routes:
        temp = val[0][:-2].split(".")
        tempstring = ''
        for value in temp:
            binarystring = "{0:b}".format(int(value))
            while(len(binarystring) != 4):
                binarystring = "0" + binarystring
            tempstring = tempstring + binarystring

            for i in tempstring:
                if(i == '0'):
                    if(cNode.left == None):
                        cNode.left = Node()
                        cNode.left.destination = val[0]
                        cNode.left.gateway = val[1]
                        cNode.left.interface = val[2]
                    else:
                        cNode = cNode.left
                else:
                    if(cNode.right == None):
                        cNode.right = Node()
                        cNode.right.destination = val[0]
                        cNode.right.gateway = val[1]
                        cNode.right.interface = val[2]
                        break
                    else:
                        cNode = cNode.right


    dict = {}
    with open('arp.txt') as arp:
        for line in arp:
            dict[line.split(" ")[0]] = line.split(" ")[1]

    arp = {}
    with open('arp.txt') as arptxt:
        for line in arptxt:
            arp[line.split(" ")[0]] = line.split(" ")[1]

    while True:
        inp = raw_input("Enter PDU: \n")   # Get the input
        temp = inp.split(" ")
        print temp
        if (len(temp) != 7):
            break
        interface = inp[0]
        src = inp[1]
        dest = inp[2]
        protocol = inp[3]
        ttl = int(inp[4])
        srcport = inp[5]
        destport = inp[6]
        if (ttl < 1):
            print (src + "->" + dest + " discarded (TTL expired)")
        print(src)
        a = root
        while (a):
                #
                #choose a direction
                #iterate until
            print "asdf"
            a = a.left

        if inp == "":       # If it is a blank line...
            break           # ...break the loop
