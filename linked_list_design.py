class node:
    
    """ Initilization """
    def __init__(self, data):
        self.val = data
        self.next = None

class MyLinkedList:
    

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index > self.length-1:
            return -1
        elif index == 0:
            if(self.head):
                return self.head.val
            else:
                return -1
        elif index == self.length-1:
            if(self.tail):
                return self.tail.val
            else:
                return -1
        x = self.head
        ind = 0
        while(ind < index):
            x = x.next
            ind += 1
        if(ind == index):
            return x.val
        return -1
        
        
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = node(val)
        if(self.tail):
            temp.next = self.head
        else:
            if(not self.tail):
                self.tail = temp
        self.head = temp
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        temp = node(val)
        if(self.tail):
            self.tail.next = temp
        else:
            if(not self.head):
                self.head = temp
        self.tail = temp
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        elif index < 0 or index >= self.length:
            return -1
        x = self.head
        ind = 0
        while(ind < index-1):
            x = x.next
            ind += 1
        if(ind == index-1):
            temp = node(val)
            temp.next = x.next
            x.next = temp
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return 
        x = self.head
        ind = 0
        if(index == 0):
            self.head = x.next
            return
        while(ind < index-1):
            x = x.next
            ind += 1
        if(ind == index-1):
            temp = x.next
            if(self.tail == temp):
                self.tail = x
            
            x.next = temp.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)