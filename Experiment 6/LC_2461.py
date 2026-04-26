class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = {}
        left = 0
        curr_sum = 0
        best = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if right - left + 1 > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                curr_sum -= nums[left]
                left += 1

            if right - left + 1 == k and len(freq) == k:
                if curr_sum > best:
                    best = curr_sum

        return best
