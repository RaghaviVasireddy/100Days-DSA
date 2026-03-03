"""
Problem: Two Sum
Platform: LeetCode
Difficulty: Easy

Approach:
- Use a hashmap (dictionary) to store visited numbers.
- For each number, check if (target - number) exists in hashmap.

Time Complexity: O(n)
Space Complexity: O(n)

Key Learning:
- Hashing helps reduce time complexity from O(n^2) to O(n).
"""

def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[nums[i]] = i
