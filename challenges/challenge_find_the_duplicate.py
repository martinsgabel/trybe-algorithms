def find_duplicate(nums):
    nums.sort()
    for n in nums:
        if type(n) == str or len(nums) < 2 or nums[0] < 0:
            return False

    for n in range(len(nums) - 1):
        if nums[n] == nums[n + 1]:
            return nums[n]

    return False
