// https://leetcode.com/problems/reverse-linked-list/submissions/
// 206. Reverse Linked List
//
// Reverse a singly linked list.
//
// Example:
//
// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL

var reverseList = function(head) {
    let prevNode = null;
    while (head !== null) {
        let nextNode = head.next;
        head.next = prevNode;
        prevNode = head;
        head = nextNode;
    }
    return prevNode;
};
