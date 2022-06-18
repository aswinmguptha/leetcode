class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target > nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1
        
print(Solution.search("Testcase 1",[-1,0,3,5,9,12],9))
print(Solution.search("Testcase 2",[-1,0,3,5,9,12],2))