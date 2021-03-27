https://leetcode.com/problems/palindrome-linked-list/
234. Palindrome Linked List

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
            
        return arr == arr[::-1]