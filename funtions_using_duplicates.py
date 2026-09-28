def remove_duplicates(nums):
    duplicate_list = []

    for i in range(len(nums)):
        if nums[i] not in nums[:i]:
            duplicate_list.append(nums[i])

    return duplicate_list


print(remove_duplicates([3, 1, 3, 2, 1]))  # [3, 1, 2]
remove_duplicates([4, 4, 4])        # [4]
print(remove_duplicates([]))               # []

