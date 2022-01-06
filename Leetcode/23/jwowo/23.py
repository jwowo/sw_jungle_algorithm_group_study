# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        head = curr = ListNode(0)
        
        for list_ in lists:
            while list_:
                res.append(list_.val)
                list_ = list_.next
                
        res.sort()
        
        for x in sorted(res):
            curr.next = ListNode(x)
            curr = curr.next
            
        return head.next