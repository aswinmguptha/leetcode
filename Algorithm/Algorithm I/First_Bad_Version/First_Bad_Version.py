class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            pivot = (left + right ) // 2
            if isBadVersion(pivot):
                right = pivot - 1
            else:
                left = pivot + 1
        return left

def isBadVersion(v):
    if v==4:
        return True
    else:
        return False
        
#print(Solution.firstBadVersion("Testcase 1 [expected = 4]: ",5))
print(Solution.firstBadVersion("Testcase 2 [expected = 2]: ",3)) #v=2