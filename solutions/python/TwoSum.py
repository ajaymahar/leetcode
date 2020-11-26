class Solution:
    def twoSum(self, nums, target):
        '''
        Method-1: Bruteforce

        time compx: O(n^2)
        space compx: O(1)

        def twoSum(self, nums, targer):
            """TODO: Docstring for bruteForceTwoSum.

            :function: twoSum()
            :returns: List of index

            """

        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i, j]


        Method-2:
        time conplex: O(n) -> in worst case we have to visit all the element
        from the list.
        space compx: O(n)

        approach would be
        1. create empty dict to keep track of visited numbers.
        2. loop through all the elements from the list and get
            the index and item
        3. check if target - curent-numner present in dict
        4. if yes then simply return the stored index and current index.
        5. if not then store the current value and index to the dict.

        '''

        visited = {}
        for idx, num in enumerate(nums):
            if target - num in visited:
                return [visited.get(target - num), idx]
            visited[num] = idx


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
