"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

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
        if not l1:
            return l2
        elif not l2:
            return l1
        elif not l1 and not l2:
            d1 = ListNode(0)
            d1.next = ListNode(0)
            d1.next.next = ListNode(0)
            return d1
        carry = 0
        s1 = ListNode(0)
        counter = 0
        sum_ = None
        while (l1 and l2):
            val = l1.val + l2.val + carry
            if val >= 10:
                val %= 10
                carry = 1
            else:
                carry = 0
            s1.val = val
            if not counter:
                sum_ = s1
            l1 = l1.next
            l2 = l2.next
            if (l1 or l2):
                s1.next = ListNode(0)
                s1 = s1.next
                counter = 1
        while l1:
            val = l1.val + carry
            if val >= 10:
                val %= 10
                carry = 1
            else:
                carry = 0
            s1.val = val
            l1 = l1.next
            if l1:
                s1.next = ListNode(0)
                s1 = s1.next
        while l2:
            val = l2.val + carry
            if val >= 10:
                val %= 10
                carry = 1
            else:
                carry = 0
            s1.val = val
            l2 = l2.next
            if l2:
                s1.next = ListNode(0)
                s1 = s1.next
        if carry:
            s1.next = ListNode(1)
        return sum_