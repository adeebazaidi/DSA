# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s1=[]
        s2=[]
        while l1:
            s1.append(str(l1.val))
            l1 = l1.next

        while l2:
            s2.append(str(l2.val))
            l2 = l2.next
        
        a=self.reversefunc(s1)
        b=self.reversefunc(s2)
        total=a+b
        c=str(total)[::-1]

        l3 = ListNode(int(c[0]))
        temp = l3

        for i in range(1, len(c)):
            temp.next = ListNode(int(c[i]))
            temp = temp.next

        return l3


    def reversefunc(self, n):
        return int("".join(n[::-1]))  