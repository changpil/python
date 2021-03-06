# n a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once.
# Find the two numbers that appear only once.


def find_single_numbers(nums):
    s = set()
    for num in nums:
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    return list(s)

def find_single_numbersXOR(nums):
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    # get the rightmost bit that is '1'
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    num1, num2 = 0, 0

    for num in nums:
        if (num & rightmost_set_bit) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num

    return [num1, num2]



def main():
  print('Single numbers are:' +
        str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

  print('Single numbers are:' +
        str(find_single_numbersXOR([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbersXOR([2, 1, 3, 2])))
main()