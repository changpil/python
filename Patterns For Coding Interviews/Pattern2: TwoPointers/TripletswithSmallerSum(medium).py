# Problem Statement #
# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
#
# Example 1:
#
# Input: [-1, 0, 2, 3], target=3
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
# Example 2:
#
# Input: [-1, 4, 2, 1, 3], target=5
# Output: 4
# Explanation: There are four triplets whose sum is less than the target:
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]


def smallerSum(arr, t):
    arr.sort()

    i, l, r = 0,0,0
    count  = 0

    while i < len(arr):
        l = i +1
        r = len(arr) - 1
        while l < r:
            _sum = arr[i] + arr[l] + arr[r]
            # Incorrect
            # if _sum < t:
            #     count += 1
            #     print(f"{arr[i]} {arr[l]} {arr[r]}")
            # else:
            #     l+= 1
            # r -= 1
            if _sum < t:
                # Add all possible smaller combination
                count += r - l
                break
            else:
                r -= 1
        i += 1
    return count

print(smallerSum([-1, 0, 2, 3], 3))
print(smallerSum([-1, 4, 2, 1, 3], 5))

