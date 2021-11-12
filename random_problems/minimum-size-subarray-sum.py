# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        array_size = len(nums)
        left_pointer = 0 
        subarray_sum = 0 
        ans = None 
        for i in range(array_size):
            subarray_sum += nums[i]
            while(subarray_sum >= target):

                if ans == None : 
                    ans = i + 1 - left_pointer 

                ans = min(ans, i + 1 - left_pointer)
                subarray_sum -= nums[left_pointer]
                left_pointer += 1

        return 0 if ans == None else ans  





if __name__ == '__main__':
        X  = Solution()
        target = 7
        nums = [2,3,1,2,4,3]        
        X.minSubArrayLen(target,nums)