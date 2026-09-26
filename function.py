

def count_even(nums):

    count = 0
    for char in nums:
        if char % 2 == 0:
            count += 1
    return count

print(count_even([2, 5, 8, 9]))
print(count_even([-4, 0, 7]))
print(count_even([]))