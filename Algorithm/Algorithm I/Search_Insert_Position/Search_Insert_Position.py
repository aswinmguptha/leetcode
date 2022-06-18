class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return left

print(Solution.searchInsert("Testcase 1", nums=[1,3,5,6],target=5))
print(Solution.searchInsert("Testcase 2", nums=[1,3,5,6],target=2))
print(Solution.searchInsert("Testcase 3", nums=[1,3,5,6],target=7))