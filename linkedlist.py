from os import system

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None        

    def insert_begin(self, data: int) -> None:
        """Inserting the node at the beginning of the linked list"""
        # create new node
        new_node = Node(data)
        # change the new_node link to the current head's link
        new_node.next = self.head
        # change the head value to new_node
        self.head = new_node

    def insert_end(self, data: int) -> None:
        """Inserting the node at the end of the linked list"""
        # create a new node
        new_node = Node(data)
        # assign the head to temp
        temp = self.head
        # base condition: if list is empty, then assign the new_node to head
        if temp == None:
            self.head = new_node
            return
        # move until last node by checking next field of all nodes
        while temp.next != None:
            temp = temp.next
        # assign the new_node address to the last node of the list
        temp.next = new_node

    def insert_after(self, data: int, key: int) -> None:
        """Inserting a node after the given the node of the linked list"""
        # create a temp node with head address
        temp = self.head
        # iterate through the list if node found break out of loop if not found then break out of loop
        while temp != None:
            if temp.data == key:
                break
            temp = temp.next
        # if it has reached last node i.e node not found
        if temp == None:
            print("\nThe node entered is not present in the linked list!")
        else:
            # if node found then create a new_node
            new_node = Node(data)
            # assign next of temp i.e previous node to the new node 
            new_node.next = temp.next
            # assign the new_node address to the next of temp 
            temp.next = new_node
        
    def insert_before(self, data: int, key: int) -> None:
        """Inserting a node before the given the node of the linked list"""
        # create a temp node with head address
        temp = self.head
        # iterate through the list if node found break out of loop if not found then break out of loop
        while temp != None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # if it has reached last node i.e node not found
        if temp == None:
            print("\nThe node entered is not present in the linked list!")
        else:
            new_node = Node(data)
            new_node.next = temp
            prev.next= new_node
        
    def delete_last(self) -> None:
        """Deleting last node of the linked list"""
        # if head is None there is no node to delete
        if self.head == None:
            print("\nThe LinkedList is empty, element cannot be deleted!")
        # if list has only one node then assign head as None
        elif self.head.next == None:
            self.head = None
            print("\nThe last node has been deleted!")
        else:
            # create a temp node to store the head of the node
            temp = self.head
            # move to the last node by checking the next of each node is none
            while temp.next != None:
                # create a previous node for the last node to store the value
                prev = temp
                temp = temp.next
            # set the next of prevoious node to none so that last node is deleted
            temp = None
            prev.next = None
            print("\nThe last node has been deleted!")

    def delete_first(self) -> None:
        """Deleting first node of the linked list"""
        # if linkedlist is empty
        if self.head == None:
            print("\nThe LinkedList is empty, element cannot be deleted!")
        # if element is present, then assign next of head to head
        else:
            self.head = self.head.next
            print("\nThe first node has been deleted!")

    def delete_node(self, key):
        """Deleting the particular node of the LinkedList"""
        # initialize temp with head
        temp = self.head
        # if the node to be deleted is first node
        if temp != None and temp.data == key:
            # assign the next of the head to next and free temp
            self.head = temp.next
            temp = None
            print(f"\nThe node {key} has been deleted")
            
        else:
            # create a temporary prev node to store the previous node data
            prev = None
            # move until key is found
            while temp != None and temp.data != key:
                # assign the temp to prev 
                prev = temp
                temp = temp.next

            # if the node is not found and reached the last node
            if temp == None:
                print(f"\n{key} node is not in the list, cannot delete!")
            else:
                # assign the prev node with next of the deleted node
                prev.next = temp.next
                # free the temp node
                temp = None
                print(f"\nThe node {key} has been deleted")

    def start(self)-> None:
        system('cls')
        while True:
            try:
                choice = int(input("\n1. Insert at beginning\n2. Insert at end\n3. Insert after given node\n4. Insert before given node\n5. Delete last node\n6. Delete first node\n7. Delete particular node\n8. Move Last node to First position\n9. Move First node to Last position\n10. Traverse and Print\n11. Exit\nEnter your choice: "))
            except:
                print("\nEnter a valid integer option!")
                continue

            # this is to check whether the entered integer is valid or not
            if choice in [1, 2, 3, 4]:
                while True:
                    try:
                        data = int(input("\nEnter the key to insert: "))
                        break  # Exit loop if input is valid
                    except ValueError:
                        print("\nEnter a valid integer!")

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
                self.delete_last()
            
            elif choice == 6:
                self.delete_first()

            elif choice == 7:
                while True:
                        try:
                            key = int(input("Enter the the value of node to delete: "))
                            break
                        except ValueError:
                            print("Enter valid integer node!")
                self.delete_node(key)
                
            elif choice == 8:
                self.make_last_first()
                
            elif choice == 9:
                self.make_first_last()

            elif choice == 10:
                self.print_list()

            elif choice == 11:
                break
            else:
                print("Enter valid input!")

LL1 = LinkedList()
LL1.start()