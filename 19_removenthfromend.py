class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        arr = []
        i = head
        if head.next is None:
            return None
        while True:
            if i.next is not None:
                arr.append(i)
            else:
                arr.append(i)
                break
            i = i.next
        if len(arr) <= 1:
            return arr[0]
        elif n == 1:
            arr[(len(arr) - n - 1)].next = None
        elif n == len(arr):
            head = arr[1]
        else:
            arr[(len(arr) - n - 1)].next = arr[len(arr) - n + 1]
        return head

# Test case
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)


s = Solution
print(s.removeNthFromEnd(s, l1, 2))