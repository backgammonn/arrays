# Design an optimal algorithm for checking whether a given string is a palindrome or not.

def is_palindrome(s):
    #string into a list of characters
    original_string = s
    reversed_string = reverse(s)

    if original_string == reversed_string:
        return True

    return False

def reverse(data):

    # string into a list of characters
    data = list(data)

    start_index = 0
    end_index = len(data) - 1

    while end_index > start_index:
        # keep swapping items
        data = list(data)
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
    # transform list of letters into a string
    return ''.join(data)


if __name__ == '__main__':
    print(is_palindrome('dad'))