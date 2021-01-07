'''
1480. Running Sum of 1d Array

https://leetcode.com/problems/running-sum-of-1d-array/

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.



Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

'''


class Solution:
    def runningSum(self, nums: list) -> list:
        '''Time: O(n) where n is numbers in a list.
           Space: O(1)
        '''
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx - 1]
        return nums


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.runningSum([3, 1, 2, 10, 1]))
