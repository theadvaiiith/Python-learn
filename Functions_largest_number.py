def find_largest(nums):

    largest = nums[0]            #usage of indexing is a must because of the -tive numbers.

    for num in nums:
        if num > largest:
            largest = num
    return largest

print(find_largest([3, 9, 2, 7]))   # 9
print(find_largest([-8, -3, -12])) # -3
find_largest([5])            # 5