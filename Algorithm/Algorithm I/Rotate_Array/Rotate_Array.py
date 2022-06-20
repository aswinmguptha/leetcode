class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        reverse(nums, 0, len(nums) - k - 1)
        reverse(nums, len(nums) - k, len(nums) - 1)
        reverse(nums, 0, len(nums) - 1)
        return nums

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

print(Solution.rotate("Testcase 1", [1,2,3,4,5,6,7], 3))
print(Solution.rotate("Testcase 2", [-1,-100,3,99], 2))