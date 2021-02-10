# Find duplicates in a one-dimensional array of integers in O(n) run time
# where integer values are smaller than the length of the array

def duplicates_array(nums):
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print('Repetition found: %s' % str(abs(num)))

if __name__ == '__main__':
    # this method cannot handle values < 0 !!
    # the maximum item is smaller than the size of the list
    n = [2, 6, 5, 1, 4, 3, 2]
    duplicates_array(n)