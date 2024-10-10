# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_obj = ListNode()
        new_node = node_obj

        carry = 0
        while l1 or l2 or carry:
            value_1 = l1.val if l1 else 0
            value_2 = l2.val if l2 else 0

            addition = value_1 + value_2 + carry
            carry = addition // 10
            addition = addition % 10
            new_node.next = ListNode(addition)

            new_node = new_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return node_obj.next


# Creating Nodes
node_one = ListNode(2)
node_one = ListNode(4, node_one)
node_one = ListNode(3, node_one)

node_two = ListNode(5)
node_two = ListNode(6, node_two)
node_two = ListNode(4, node_two)

solution = Solution()
answer = solution.addTwoNumbers(node_one, node_two)

# Printing result in readable format
output = []
while answer:
    output.append(answer.val)
    answer = answer.next

print(output)
