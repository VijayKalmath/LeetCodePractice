class Solution:
    def maxAscendingSum(self, nums) -> int:
        fast_pointer = 0 
        max_value = [nums[0]]
        while(fast_pointer < len(nums) -1 ):
            if nums[fast_pointer + 1 ] > nums[fast_pointer] : 
                max_value[-1] += nums[fast_pointer + 1 ]
            else : 
                max_value.append(nums[fast_pointer + 1])
            fast_pointer +=1
        return max(max_value)