import readFAT

# Create an empty dictionary for fat
netFat = {}

# Adds an entry to the fat
# Fails if there is already an entry bearing the same name
# file name, file size, block1 nodes, block2 nodes, block3 nodes, block4 nodes


def addEntry(name, size, nodes1, nodes2, nodes3, nodes4):
    if name not in netFat:
        block1, block2, block3, block4 = nodes1, nodes2, nodes3, nodes4
        netFat[name] = [name, size, block1, block2, block3, block4]

# 0,(Name),(Size),(Nodes with block 1),...,(Nodes with block 2)
# the upd variable decides whether to update an existing entry instead


def addHandler(line, upd):
    temp = ""
    start = True
    inP = False
    isName = False
    isSize = False
    isB1 = False
    isB2 = False
    isB3 = False
    isB4 = False
    name = ""
    size = 0
    b1, b2, b3, b4 = [], [], [], []
    for i in line:
        if start == True and i == '(':
            start = False
            isName = True
        elif isName == True and i != '(' and i != ')' and i != ',':
            temp = temp + i
        elif isName == True and i == '(':
            isName = False
            isSize = True
            name = temp
            temp = ""
        elif isSize == True and i != '(' and i != ')' and i != ',':
            temp = temp + i
        elif isSize == True and i == '(':
            inP = True
            isSize = False
            isB1 = True
            size = int(temp)
            temp = ""
        elif isB1 == True and i != '(' and i != ')' and i != ',':
            temp = temp + i
        elif isB1 == True and i == ',' and inP == True:
            b1.append(int(temp))
            temp = ""
        elif isB1 == True and i == ')':
            b1.append(int(temp))
            inP = False
            temp = ""
        elif isB1 == True and i == '(':
            inP = True
            isB1 = False
            isB2 = True
            temp = ""
        elif isB2 == True and i != '(' and i != ')' and i != ',':
            temp = temp + i
        elif isB2 == True and i == ',' and inP == True:
            b2.append(int(temp))
            temp = ""
        elif isB2 == True and i == ')':
            inP = False
            b2.append(int(temp))
            temp = ""
        elif isB2 == True and i == '(':
            inP = True
            isB2 = False
            isB3 = True
            temp = ""
        elif isB3 == True and i != '(' and i != ')' and i != ',':
            temp = temp + i
        elif isB3 == True and i == ',' and inP == True:
            b3.append(int(temp))
            temp = ""
        elif isB3 == True and i == ')':
            inP = False
            b3.append(int(temp))
            temp = ""
        elif isB3 == True and i == '(':
            inP = True
            isB3 = False
            isB4 = True
            temp = ""
        elif isB4 == True and i != '(' and i != ')' and i != ',':
            temp = temp + i
        elif isB4 == True and i == ',' and inP == True:
            b4.append(int(temp))
            temp = ""
        elif isB4 == True and i == ')':
            inP = False
            b4.append(int(temp))
    if upd == 0:
        addEntry(name, size, b1, b2, b3, b4)
    elif upd == 1:
        updateEntry(name, size, b1, b2, b3, b4)

# Deletes an entry in the fat
# file name


def delEntry(name):
    if name in netFat:
        targetEntry = netFat.pop(name)


def delHandler(line):
    name = ""
    start = True
    isName = False
    for i in line:
        if start == True and i == '(':
            start = False
            isName = True
        elif isName == True and i != ')':
            name = name + i
        elif isName == True and i == ')':
            break
    delEntry(name)

# Updates an entry in the fat
# Fails if there is no such entry
# file name, file size, block1 nodes, block2 nodes, block3 nodes, block4 nodes


def updateEntry(name, size, nodes1, nodes2, nodes3, nodes4):
    if name in netFat:
        block1, block2, block3, block4 = nodes1, nodes2, nodes3, nodes4
        netFat[name] = [name, size, block1, block2, block3, block4]

# Returns a list of nodes that hold the designated block for the given file
# file name, # of desired block


def getNodesWithBlock(name, blockNum):
    if name in netFat:
        temp = netFat[name][blockNum + 1]
        return temp

# Returns the file size of a given file
# file name


def getFileSize(name):
    if name in netFat:
        return netFat[name][1]

# Used when a node deletes certain blocks
# Removes the node from block entries
# file name, node #, list of deleted blocks


def removeNode(name, node, deletedBlocks):
    if name in netFat:
        for i in deletedBlocks:
            if node in netFat[name][i + 1]:
                netFat[name][i+1].remove(node)

# Used when a new node stores certain blocks
# Adds the node when not already stored
# file name, node #, list of added blocks


def addNode(name, node, addedBlocks):
    if name in netFat:
        for i in addedBlocks:
            if node not in netFat[name][i+1]:
                netFat[name][i+1].append(node)

# Writes the fat to a file "fAT.txt"


def writeFat(target):
    # creates a file titled nFat.txt
    # w+ indicates write permissions and generation of a new file if not there
    f = open(target, "w+")
    # for i in range(20):
    for i in netFat:
        name = "(" + netFat[i][0] + "),"
        size = "({size}),".format(size=netFat[i][1])
        b1, b2, b3, b4 = "(", "(", "(", "("
        temp = str(len(netFat[i][2]))
        b1 = b1 + temp
        temp = str(len(netFat[i][3]))
        b2 = b2 + temp
        temp = str(len(netFat[i][4]))
        b3 = b3 + temp
        temp = str(len(netFat[i][5]))
        b4 = b4 + temp
        for j in netFat[i][2]:
            temp = str(j)
            b1 = b1 + "," + temp
        for j in netFat[i][3]:
            temp = str(j)
            b2 = b2 + "," + temp
        for j in netFat[i][4]:
            temp = str(j)
            b3 = b3 + "," + temp
        for j in netFat[i][5]:
            temp = str(j)
            b4 = b4 + "," + temp
        b1 = b1 + "),"
        b2 = b2 + "),"
        b3 = b3 + "),"
        b4 = b4 + ")"
        # print(name,size,b1,b2,b3,b4)
        f.write(name + size + b1 + b2 + b3 + b4)
        f.write("\r")
    f.close()

# Reads in the current fat
# Accepts input file and updates fat with values
# (name),(size),(#nodes with block1, nodes with block1),...,(same with block4)


def readFat():
    # open file in read mode
    f = open("fat.txt", "r")
    netFat.clear()
    for line in f:
        workingLine = line.strip()
        temp = ""
        start = True
        inP = False
        isName = False
        isSize = False
        isB1 = False
        isB2 = False
        isB3 = False
        isB4 = False
        name = ""
        size = 0
        b1, b2, b3, b4 = [], [], [], []
        for i in workingLine:
            if start == True and i == '(':
                start = False
                isName = True
            elif isName == True and i != '(' and i != ')' and i != ',':
                temp = temp + i
            elif isName == True and i == '(':
                isName = False
                isSize = True
                name = temp
                temp = ""
            elif isSize == True and i != '(' and i != ')' and i != ',':
                temp = temp + i
            elif isSize == True and i == '(':
                inP = True
                isSize = False
                isB1 = True
                size = int(temp)
                temp = ""
            elif isB1 == True and i != '(' and i != ')' and i != ',':
                temp = temp + i
            elif isB1 == True and i == ',' and inP == True:
                b1.append(int(temp))
                temp = ""
            elif isB1 == True and i == ')':
                b1.append(int(temp))
                inP = False
                temp = ""
            elif isB1 == True and i == '(':
                inP = True
                isB1 = False
                isB2 = True
                temp = ""
            elif isB2 == True and i != '(' and i != ')' and i != ',':
                temp = temp + i
            elif isB2 == True and i == ',' and inP == True:
                b2.append(int(temp))
                temp = ""
            elif isB2 == True and i == ')':
                inP = False
                b2.append(int(temp))
                temp = ""
            elif isB2 == True and i == '(':
                inP = True
                isB2 = False
                isB3 = True
                temp = ""
            elif isB3 == True and i != '(' and i != ')' and i != ',':
                temp = temp + i
            elif isB3 == True and i == ',' and inP == True:
                b3.append(int(temp))
                temp = ""
            elif isB3 == True and i == ')':
                inP = False
                b3.append(int(temp))
                temp = ""
            elif isB3 == True and i == '(':
                inP = True
                isB3 = False
                isB4 = True
                temp = ""
            elif isB4 == True and i != '(' and i != ')' and i != ',':
                temp = temp + i
            elif isB4 == True and i == ',' and inP == True:
                b4.append(int(temp))
                temp = ""
            elif isB4 == True and i == ')':
                inP = False
                b4.append(int(temp))
        addEntry(name, size, b1, b2, b3, b4)
    f.close()

# Updates fat with values from update.txt
# 0,(Name),(Size),(Nodes w/ block 1),...,(Nodes w/ block 4)
# 1,(Name)
# 2,(Name),(Size),(Nodes w/ block 1),...,(Nodes w/ block 4)
# 0 to add an entry, 1 to nuke an entry


def updateFat():
    # open file in read mode
    f = open("update.txt", "r")
    for line in f:
        workingLine = line.strip()
        for i in workingLine:
            if i == "0":
                addHandler(workingLine, 0)
                break
            elif i == "1":
                delHandler(workingLine)
                break
            elif i == "2":
                addHandler(workingLine, 1)
                break
    f.close()
    open("update.txt", "w").close()
    writeFat("fat.txt")


readFat()
writeFat("backup.txt")
updateFat()
readFAT.add_block_from_file()
