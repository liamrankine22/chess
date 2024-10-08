class Node:
    """
    Class for creating nodes containing data

    Attributes:
        data (type): Data that will be stored in the node
        next (Node): The connecting next node

    """
    def __init__(self, data, x_pos, y_pos):
        """
        Initializes the Node with data

        :param data: data that will be stored in the node
        """
        self.data = data
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.next = None

class SelectedPieces:
    """
    Modified singly linked list used for storing pieces

    Attributes:
        head (Node): the head of the singly linked list

    Methods:
        add_selected_piece(data) --> None
            Adds a piece into the linked list
        remove_piece() --> None
            Removes a piece from the linked list
        remove_all() --> None
            Removes every piece from the linked list
        is_empty() --> bool
            Checks if the list is empty
    """
    def __init__(self):
        """
        Initializes the linked list
        """
        self.head = None

    def add_selected_piece(self, data, x_pos, y_pos):
        """
        Adds a piece to the list

        :param y_pos: x position of the piece
        :param x_pos: y position of the piece
        :param data: data to be stored in the newly added node

        :return: None
        """
        new_node = Node(data, x_pos, y_pos)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def remove_piece(self):
        """
        Removes the first added piece

        :return: the node removed
        """
        if not self.is_empty():
            current_node = self.head
            self.head = current_node.next
            return current_node
        else:
            print("List empty")

    def remove_all(self):
        """
        Removes all pieces from the list

        :return: None
        """
        self.head = None

    def is_empty(self):
        """
        Checks if the list is empty

        :return: boolean value True or False
        """
        return self.head is None

    def iterate(self, data):
        """
        Iterates over the linked list to check if specified data is in the list

        :param data: data to be compared

        :return: Node containing the data
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None