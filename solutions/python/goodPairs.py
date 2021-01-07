'''
1512. Number of Good Pairs

https://leetcode.com/problems/number-of-good-pairs/

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

'''


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        '''
         Method -1
         Time: O(n^2)
         Space: O(1)

         count = 0
         for i in range(len(nums) -1):
              for j in range(i + 1, len(nums)):
                  if nums[i] == nums[j]:
                      count +=1
         return count
         =========================================
         Method -2
         Time: O(n log n)
         Space: O(1)

        count = 0
        i = 0
        nums.sort()                       <-- O(n log n)
        for j in range(1,len(nums)):      <-- O(n)
          if nums[i] == nums[j]:
              count += j -i
          else:
              i =j
              j +=1

        return count

        ==========================================
        Method -3  <---- Optimal Solution
        Time: O(n)
        Space: O(n)


        '''
        mapping = [0 for _ in range(101)]
        count = 0

        for num in nums:
            if mapping[num] != 0:
                count += mapping[num]
                mapping[num] += 1
            else:
                mapping[num] = 1
        return count
