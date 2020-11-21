#Tarjan's Algorithm
'''https://leetcode.com/problems/critical-connections-in-a-network/discuss/382526/Tarjan-Algorithm-(DFS)-Python-Solution-with-explanation
'''
from collections import defaultdict
class Solution:
    def criticalConnections(self, n, connections):
        if n < 1:
            return connections[0]

        #build graph
        graph = defaultdict(list)
        for edges in connections:
            graph[edges[0]].append(edges[1])
            graph[edges[1]].append(edges[0])

        
sol = Solution()
sol.criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]])