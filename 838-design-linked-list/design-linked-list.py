class MyLinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.val  # Return value at the index
            current = current.next  # Move to the next node
            count += 1
        return -1  # Index out of range

    def addAtHead(self, val: int) -> None:
        newnode = type('', (), {})()  # Create an empty object dynamically
        newnode.val = val
        newnode.next = self.head  # Point to current head
        self.head = newnode  # Update head to new node

    def addAtTail(self, val: int) -> None:
        newnode = type('', (), {})()
        newnode.val = val
        newnode.next = None
        if not self.head:  # If list is empty, set new node as head
            self.head = newnode
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = newnode  # Attach new node at the end

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        current = self.head
        count = 0
        while current:
            if count == index - 1:
                newnode = type('', (), {})()
                newnode.val = val
                newnode.next = current.next
                current.next = newnode  # Insert new node at index
                return
            current = current.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:  # Delete head node
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current.next:
            if count == index - 1:
                current.next = current.next.next  # Remove node at index
                return
            current = current.next
            count += 1
        