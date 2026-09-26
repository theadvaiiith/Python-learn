

def sum_even(nums):

    total = 0


    for num in nums:
        if num % 2 == 0:
            total = total + num

    return total


print(sum_even([2, 5, 8, 9]))  # 10
print(sum_even([-4, 0, 7]))    # -4
print(sum_even([]))            # 0