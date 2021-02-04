#Given an array, return the reverse of an array in O(n) linear time complexity and in-place.
#For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

def reverse(nums):
    #pointing to the first item
    start_index = 0
    end_index = len(nums)-1

    while end_index > start_index:
        # keep swapping items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

if __name__ == '__main__':
    n = [1, 2, 3, 4, 5]
    reverse(n)
    print(n)