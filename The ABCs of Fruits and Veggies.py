# Steven Nelson
# November 8th, 2022
# CSC 242 - Lab Assignment 11


def queue_intro():
    """the main introduction to the program that welcomes the user to the application."""

    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    print("* Welcome to the ABCs of Fruits & Veggies Linked Queue, it is a pleasure to see you today!!!")
    print("* The goal is to make a queue from A to Z with the names of fruits and veggies of the world:")


class Node:
    """a class for the Nodes"""

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_Queue:
    """the main linked queue class that will handle the enqueue and dequeue operations along with iteration"""

    def __init__(self):
        self.head = None
        self.last_node = None

    def enqueue(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            val_returned = self.head.data
            self.head = self.head.next
            return val_returned

    def iterate_item(self):
        # iterate through the list
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def clear(self):
        self.head = None
        self.last_node = None


my_instance = Linked_Queue()
queue_intro()
while True:
    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    print("* If you would like to add a fruit or veggie to the linked queue please enter 'enqueue <name>'")
    print("* If you would like to remove the first item of the queue please type 'dequeue'")
    print("* If you would like to view all items currently in the queue please type 'display'")
    print("* If you would like to see if a certain item is currently in the queue type 'locate <name>'")
    print("* If you would like to clear the linked queue and start with a fresh queue type 'clear'")
    print("* If you finished and would like to exit the program please type 'exit' to leave, thank you!!")
    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    my_input = input("Which option above would you like to do with the ABCs linked queue? ").split()

    user_input = my_input[0].strip().lower()
    if user_input == "enqueue":
        print(f"The element '{str(my_input[1])}' has been added to the fruits & veggies queue.")
        my_instance.enqueue(str(my_input[1]))
    elif user_input == "dequeue":
        dequeued = my_instance.dequeue()
        if dequeued is None:
            print('The queue is empty.')
        else:
            print(f"The dequeued fruit or veggie '{str(dequeued)}' has left the queue")
    elif user_input == "display":
        for val in my_instance.iterate_item():
            print(val)
    elif user_input == "locate":
        if str(my_input[1]) in my_instance.iterate_item():
            print(f"The element '{str(my_input[1])}' is currently in the linked queue.")
        else:
            print("The item is not currently in the linked queue.")
    elif user_input == "clear":
        my_instance.clear()
    elif user_input == "exit":
        print("Thank you for using the fruits and veggies queue, we hope you have a wonderful day.")
        exit()
    else:
        print("Please enter an input from the application selection choices, thank you")


