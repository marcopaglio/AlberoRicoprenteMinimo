class Node:
    def __init__(self, initData, rap):
        self.data = initData
        self.next = None
        self.delegate = rap

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def getDelegate(self):
        return self.delegate

    def setDelegate(self, newDelegate):
        self.delegate = newDelegate


class LinkedList:
    def __init__(self):
        self.head = None
        self.queue = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    #non usato
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def printList(self):
        current = self.head
        while current is not None:
            print('..',current.getData())
            current = current.getNext()

    def add(self, item):
        if self.isEmpty():
            temp = Node(item, item)
            self.head = temp
        else:
            temp = Node(item, self.head)      #il rappresentante è in testa
            self.queue.setNext(temp)
        self.queue = temp

    #non utilizzato, preferibile clear
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is not None and current.getNext() is not None:   #generico elemento interno alla lista
            previous.setNext(current.getNext())
        else:
            if previous is None:                   #se è l'elemento in testa
                self.head = current.getNext()
                self.updateDelegate()
            if current.getNext() is None:          #se è l'elemento in coda
                self.queue = previous
        return current

    #non utilizzato perchè chiamato da remove
    def updateDelegate(self):
        current = self.head
        while current is not None:
            current.setDelegate(self.head)
            current = current.getNext()

    def getHead(self):
        return self.head

    def getDelegate(self):
        return self.head.getData()

    def clear(self):
        self.head = None
        self.queue = None

