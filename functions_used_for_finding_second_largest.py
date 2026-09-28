def second_largest(nums):

    if nums == []:
        return None

    largest = nums[0]
    second_largest = None



    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num

        elif num < largest and (second_largest is None or num > second_largest):
            second_largest = num


    return second_largest


print(second_largest([3, 9, 2, 7]))   # 7
print(second_largest([5, 5, 1]))      # 1
print(second_largest([-8, -3, -12]))  # -8
print(second_largest([4, 4]))         # None