# https://leetcode.com/problems/reverse-linked-list/submissions/
# 206. Reverse Linked List
#
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
# Same problem as my js-practice-problem-17.js, instead I will be using recursion for my python Solution


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        newNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newNode
