class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        totalSum = sum(nums)
        r = totalSum % p

        if r == 0:
            return 0

        prefix = 0
        hashmap = {0: -1}
        minLength = len(nums)

        for i in range(len(nums)):

            prefix += nums[i]
            cur = prefix % p

            target = (cur - r + p) % p

            if target in hashmap:
                minLength = min(minLength, i - hashmap[target])

            hashmap[cur] = i

        if minLength == len(nums):
            return -1
        else:
            return minLength
