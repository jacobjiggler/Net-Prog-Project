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
    routes = filter(None, routes)
    root = Node()
    cNode = root
    temp = []
    for val in routes:
        cNode = root
        temp = val[0].split("/")
        depth = int(temp[1])
        temp = temp[0].split(".")
        tempstring = ''
        for value in temp:
            binarystring = "{0:b}".format(int(value))
            while(len(binarystring) != 8):
                binarystring = "0" + binarystring
            tempstring = tempstring + binarystring

        count = 1
        for i in tempstring:
            if(i == '0'):
                if(cNode.left == None):
                    cNode.left = Node()

                cNode = cNode.left
            else:
                if(cNode.right == None):
                    cNode.right = Node()

                cNode = cNode.right
            if(count == depth):
                break
            count = count + 1

        cNode.destination = val[0]
        cNode.gateway = val[1]
        cNode.interface = val[2]


    arp = {}
    with open('arp.txt') as arptxt:
        for line in arptxt:
            arpline = line.split(" ")
            arpline = filter(None, arpline)
            arp[arpline[0]] = arpline[1]

    while True:
        inp = raw_input("Enter PDU: \n")   # Get the input
        if inp == "":       # If it is a blank line...
            break           # ...break the loop
        temp = inp.split(" ")
        temp = filter(None, temp)
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
        if (ttl <= 1):
            print (src + ":" + srcport + "->" + dest + ":" + destport + " discarded (TTL expired)")
        else:
            tempstring = ''
            temp = dest.split(".")
            for value in temp:
                binarystring = "{0:b}".format(int(value))
                while(len(binarystring) != 8):
                    binarystring = "0" + binarystring
                tempstring = tempstring + binarystring

            cNode = root
            for i in tempstring:
                if(i == '0'):
                    print "left"
                    if(cNode.left == None):
                        break
                    else:
                        cNode = cNode.left
                else:
                    print "right"
                    if(cNode.right == None):
                        break
                    else:
                        cNode = cNode.right


            #if direct point to point
            if (cNode.gateway == "0.0.0.0"):
                #routing table lookup
                print (src + ":" + srcport + "->" + dest + ":" + destport + " directly connected " + "(" + cNode.interface + "-" + arp[dest] +") ttl " + str(ttl - 1))
            else:
                #this is wrong
                #arp lookup
                print cNode.gateway
                if (arp.get(cNode.gateway)):
                    print (src + ":" + srcport + "->" + dest + ":" + destport + " via " + cNode.gateway + "(" + interface + "-" + arp[cNode.gateway] +") ttl " + str(ttl - 1))
                else:
                    print (src + "->" + dest + " discarded (destination unreachable)")
