def is_sorted(nums):

    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return False

    return True


print(is_sorted([1, 2, 2, 5]))  # True
is_sorted([3, 1, 4])     # False
is_sorted([7])           # True
is_sorted([])            # True