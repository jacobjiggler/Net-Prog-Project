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
        temp = val[0].split("/")
        temp = temp[0].split(".")
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
                    break
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

    arp = {}
    with open('arp.txt') as arptxt:
        for line in arptxt:
            arp[line.split(" ")[0]] = line.split(" ")[1]

    while True:
        inp = raw_input("Enter PDU: \n")   # Get the input
        if inp == "":       # If it is a blank line...
            break           # ...break the loop
        temp = inp.split(" ")
        print temp
        if (len(temp) != 7):
            break
        interface = temp[0]
        src = temp[1]
        dest = temp[2]
        protocol = temp[3]
        ttl = int(temp[4])
        srcport = temp[5]
        destport = temp[6]
        if (ttl < 1):
            print (src + "->" + dest + " discarded (TTL expired)")
        tempstring = ''
        temp = dest[0].split("/")
        temp = temp[0].split(".")
        for value in temp:
            binarystring = "{0:b}".format(int(value))
            while(len(binarystring) != 4):
                binarystring = "0" + binarystring
            tempstring = tempstring + binarystring
        cnode = root
        for i in tempstring:
            if(i == '0'):
                if(cNode.left == None):
                    break
                else:
                    cNode = cNode.left
            else:
                if(cNode.right == None):
                    break
                else:
                    cNode = cNode.right
        #if direct point to point
        if (cNode.gateway == "0.0.0.0" and cNode.destination.split("/")[1] == 32):
            #routing table lookup
            print (src + ":" + srcport + "->" + dest + ":" + destport + " via " + cNode.gateway + "(" + cNode.interface  +") ttl " + str(ttl - 1))
        else:
            #arp lookup
            if (arp[dest]):
                print (src + ":" + srcport + "->" + dest + ":" + destport + " via " + cNode.gateway + "(" + interface + "-" + arp[dest] +") ttl " + str(ttl - 1))
            else:
                print (src + "->" + dest + " discarded (destination unreachable)")
