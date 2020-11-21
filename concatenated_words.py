"""https://leetcode.com/problems/concatenated-words/discuss/941882/Recursion-Trie"""
# class Node:
#     def __init__(self):
#         self.children = {}
#         self.words = []
        
# class Trie:
#     def __init__(self, words):
#         self.root = Node()
#         if words:
#             self.add(words)
            
#     def add(self, words):
#         for word in words:
#             curr = self.root
#             for char in word:
#                 if char not in curr.children:
#                     curr.children[char] = Node()
#                 else:
#                     curr = curr.children[char]
        
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        words.sort(key = len)
        print(words)

sol = Solution()
sol.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])