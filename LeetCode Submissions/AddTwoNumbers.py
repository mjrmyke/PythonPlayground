'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.carry = 0
        node = root = ListNode(0)
        while l1 or l2 or self.carry:
            if l1:
                self.carry = self.carry + l1.val
                l1=l1.next
            if l2:
                self.carry = self.carry + l2.val
                l2=l2.next
            rem = self.carry%10
            node.next = node = ListNode(rem)
            self.carry = self.carry /10
        return root.next
                
            
