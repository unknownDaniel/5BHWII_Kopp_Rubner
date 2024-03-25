import random as rand


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addToEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node
        cur_node.next = node

    def __len__(self):
        if self.head is None:
            return 0
        length = 1
        cur_node = self.head
        while cur_node.next:
            length += 1
            cur_node = cur_node
        return length

    class Iterator:
        def __init__(self, head):
            self.head = head

        def __iter__(self):
            return self

        def __next__(self):
            while self.cur_node:
                data = self.cur_node.data
                self.cur_node = self.cur_node.next_node
                return data

            raise StopIteration

    def __iter__(self):
        return self.Iterator(self.head)


def main():
    llist = LinkedList()

    for i in range(9):
        llist.addToEnd(rand.randint(0, 100))

    print(len(llist))


if __name__ == '__main__':
    main()