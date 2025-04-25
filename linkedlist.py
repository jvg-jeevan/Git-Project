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