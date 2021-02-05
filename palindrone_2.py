#a word, phrase, or sequence that reads the same backward as forward
def palindrome(string):
    # Check if string equals string in reverse order
    if string == string[::-1]:
        return True
    return False

if __name__ == '__main__':
    print(palindrome('dad'))