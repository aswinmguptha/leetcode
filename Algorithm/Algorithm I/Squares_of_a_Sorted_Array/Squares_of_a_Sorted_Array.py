class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squared_array = [None for _ in nums]
        left_pointer, right_pointer = 0, len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left_pointer]) > abs(nums[right_pointer]):
                squared_array[i] = nums[left_pointer] ** 2
                left_pointer += 1
            else:
                squared_array[i] = nums[right_pointer] ** 2
                right_pointer -= 1
        return squared_array

print(Solution.sortedSquares("Testcase 1", [-4,-1,0,3,10]))
print(Solution.sortedSquares("Testcase 2", [-7,-3,2,3,11]))