class Solution:
    def intervalIntersection(self, A, B):
        a, b = 0, 0
        overlap = []
        if not A or not B :
            return overlap
        
        while a < len(A) and b < len(B):
            startA, endA = A[a][0], A[a][1]
            startB, endB = B[b][0], B[b][1]
            
            if startA <= startB and startB <= endA:
                overlap.append([startB, min(endB, endA)])
                if endA < endB:
                    a += 1
                else:
                    b += 1
            elif startB <= startA and startA <= endB:
                overlap.append([startA, min(endA, endB)])
                if endB < endA:
                    b += 1
                else:
                    a += 1
            elif startA <= startB:
                a += 1
            else:
                b += 1  
        return overlap
sol = Solution()
print(sol.intervalIntersection([[3,5],[9,20]],[[4,5],[7,10],[11,12],[14,15],[16,20]]))