class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        head = None
        tail = None
        total = 0

        for op in operations:
            if op not in ["C", "D", "+"]:
                node = Node(int(op))

                if head is None:
                    head = tail = node
                else:
                    tail.next = node
                    tail = node
                total += int(op)

            elif op == "C":
                total -= tail.data

                if head == tail:
                    head = tail = None
                else:
                    temp = head

                    while temp.next != tail:
                        temp = temp.next
                    tail = temp
                    tail.next = None

            elif op == "D":
                score = 2 * tail.data
                node = Node(score)
                tail.next = node
                tail = node
                total += score

            elif op == "+":
                second_last = head
                while second_last.next != tail:
                    second_last = second_last.next

                score = second_last.data + tail.data
                node = Node(score)
                tail.next = node
                tail = node
                total += score

        return total