def find_duplicate(nums):
    if not nums or type(nums) != str or len(nums) < 2:
        return False

    nums.sort()
    for n in range(len(nums) - 1):
        if nums[n] < 0:
            return False
        if nums[n] == nums[n + 1]:
            return nums[n]

    return False
