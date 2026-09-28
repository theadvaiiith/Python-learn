def second_largest(nums):

    largest = nums[0]

    second_largest = 0


    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num

        elif largest > num > second_largest:
            second_largest = num

    if second_largest == 0:
        return None
    


    return second_largest


print(second_largest([3, 9, 2, 7]))   # 7
print(second_largest([5, 5, 1]))      # 1
print(second_largest([-8, -3, -12]))  # -8
print(second_largest([4, 4]))         # None