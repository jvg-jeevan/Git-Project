import os
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, key: int) -> None:
        """Insert a new node at the beginning of the Doubly LinkedList."""
        # create a new node
        new_node = Node(key)
        # assign the head value to the next field of the linkedlist
        new_node.next = self.head
        # if the linkedlist is not empty then assign the prev of the head with new_node 
        if self.head != None:
            self.head.prev = new_node
        # set the head with new_node address
        self.head = new_node
        print(f"\nFirst node inserted, Successfully!")

    def insert_end(self, key: int) -> None:
        """Insert a new node at the end of the Doubly LinkedList"""
        # create a new node
        new_node = Node(key)
        # if the linked list is empty
        if self.head == None:
            self.head = new_node
        else:
            # create a temp node to traverse
            temp = self.head
            # move to the last node of the linked list
            while temp.next != None:
                temp = temp.next
            # assign the next of the last node with new_node
            temp.next = new_node
            # assign the prev of new_node with last node
            new_node.prev = temp
        print(f"\nLast node inserted, Successfully!")

    def insert_after(self, data: int, key: int) -> None:
        """Insert a new node after given node of the Doubly LinkedList"""
        if self.head == None:
            print("\nDoubly LinkedList Empty!")
        else:
            temp = self.head
            while temp != None:
                if temp.data == key:
                    break
                temp = temp.next
            new_node = Node(data)
            if temp == None:
                print(f"\nKey {key} is not present!")
            else:
                if temp.next == None:
                    temp.next = new_node
                    new_node.prev = temp
                else:
                    new_node.next = temp.next
                    temp.next.prev = new_node
                    new_node.prev = temp
                    temp.next = new_node
                print(f"\nNode has been inserted after {key}")
    
    def insert_before(self, data: int, key: int) -> None:
        """Insert a new node before given node of the Doubly LinkedList"""
        if self.head == None:
            print("\nDoubly LinkedList Empty!")
        else:
            temp = self.head
            while temp != None:
                if temp.data == key:
                    break
                temp = temp.next
            new_node = Node(data)
            if temp == None:
                print(f"\nKey {key} is not present!")
            else:
                if temp.prev == None:
                    temp.prev = new_node
                    new_node.next = temp
                else:
                    temp.prev.next = new_node
                    new_node.prev = temp.prev
                    new_node.next = temp
                    temp.prev = new_node
                print(f"\nNode has been inserted before {key}")

    def delete_first(self) -> None:
        if self.head == None:
            print("\nDoubly LinkedList Empty!")
        else:
            self.head = self.head.next
            print("\nFirst node deleted, Successfully!")

    def delete_last(self) -> None:
        if self.head == None:
            print("\nDoubly LinkedList Empty!")
        elif self.head.next == None:
            self.head = None
            print("\nLast node deleted, Successfully!")
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
            print("\nLast node deleted, Successfully!")

    def traverse_forward(self) -> None:
        """Forward Traversal from first to last node"""
        print()
        temp = self.head
        if temp == None:
            print("\nDoubly LinkedList Empty!")
        else:
            while temp != None:
                print(temp.data, end= "")
                # if there is next value then it prints -> next is none or last node it won't print ->
                if temp.next != None:
                    print(" -> ", end= "")
                temp = temp.next
        print()

    def traverse_backward(self) -> None:
        """Backward Traversal from last to first node"""
        print()
        temp = self.head
        if temp == None:
            print("\nDoubly LinkedList Empty!")
        else:
            while temp.next != None:
                temp = temp.next

            while temp != None:
                print(temp.data, end= "")
                if temp.prev != None:
                    print(" -> ", end="")
                temp = temp.prev
        print()

    def start(self) -> None:
        os.system('cls')
        while True:
            try:
                choice = int(input("\n1. Insertion at beginning\n2. Insertion at ending\n3. Insertion after a node\n4. Insertion before a node\n5. Delete first node\n6. Delete last node\n11. Forward Traversal\n12. Backward Traversal\n13. Exit\nEnter Your Choice: "))
            except:
                print("\nEnter valid Integer Choice!")
            if choice in [1, 2, 3, 4]:
                while True:
                    try:
                        data = int(input("Enter the key to insert: "))
                        break  # Exit loop if input is valid
                    except ValueError:
                        print("\nEnter a valid integer!")
                        continue
                if choice == 1:
                    self.insert_begin(data)
                elif choice == 2:
                    self.insert_end(data)
                elif choice == 3:
                    while True:
                        try:
                            key = int(input("Enter the the value of node the node to insert after: "))
                            break
                        except ValueError:
                            print("Enter valid integer node!")
                    self.insert_after(data, key)
                elif choice == 4:
                    while True:
                        try:
                            key = int(input("Enter the the value of node the node to insert before: "))
                            break
                        except ValueError:
                            print("Enter valid integer node!")
                    self.insert_before(data, key)
            elif choice == 5:
                self.delete_first()
            elif choice == 6:
                self.delete_last()
            elif choice == 11:
                self.traverse_forward()
            elif choice == 12:
                self.traverse_backward()
            else:
                break

l = DoublyLinkedList()
l.start()