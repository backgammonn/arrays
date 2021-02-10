#Construct an algorithm to check whether two words (or phrases) are anagrams or not.
def anagram(str1, str2):
    # Check if length is the same - False if not equal
    if len(str1) != len(str2):
        return False

    # Sort letters for each sting

    str1 = sorted(str1)
    str2 = sorted(str2)

    # Check if letters at indicies are the same; if not, return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


if __name__ == '__main__':

    s1 = ['f','l','u','s','t','e','r']
    s2 = ['r','e','s','t','f','u','l']

    print (anagram(s1, s2))