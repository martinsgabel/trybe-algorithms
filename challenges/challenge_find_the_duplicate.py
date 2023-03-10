def find_duplicate(nums):
    if (
        not nums
        or isinstance(nums, str)
        or len(nums) < 2
        or any(n < 0 for n in nums.sort())
    ):
        return False

    nums.sort()
    for n in range(len(nums) - 1):
        if nums[n] == nums[n + 1]:
            return nums[n]
