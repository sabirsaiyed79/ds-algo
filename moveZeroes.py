class Solution:
    def moveZero(self, nums: List[int]):
        l = 0
        for r in range(len(nums)):
            print(nums[r])
            if nums[r]:
                nums[l], nums[r] = nums[r],nums[l]
                print(nums)
                l += 1
        

