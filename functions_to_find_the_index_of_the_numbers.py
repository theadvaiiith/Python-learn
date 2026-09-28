def find_index(nums, target):

    for i in range(len(nums)):
        if nums[i] == target:

            return i

    return -1

print(find_index([4, 7, 7, 9], 7))  # 1
print(find_index([4, 7, 9], 5))     # -1
print(find_index([], 3))            # -1
