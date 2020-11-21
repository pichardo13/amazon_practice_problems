"""
https://leetcode.com/problems/merge-k-sorted-lists/
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for curr in lists:
            while curr:
                heapq.heappush(h, curr.val)
                curr = curr.next
        items = [heapq.heappop(h) for i in range(len(h))]
        
        if items:
            linkedList = ListNode(items[0])
            curr = linkedList
            for i in items[1:]:
                curr.next = ListNode(i)
                curr = curr.next
            return linkedList
        return 