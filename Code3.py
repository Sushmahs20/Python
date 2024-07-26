def fun1(string1):
    """This function takes string as the argument and returns True if input string is palindrome, False otherwise"""
    # Converting the string to lowercase
    string1 = string1.lower()
    # Checking and returning if the string is equal to the reverse of the string
    return string1 == string1[::-1]


def fun2(string2):
    """This function takes string as an argument and returns the most frequently repeated letter or digits"""
    #Converting the string into lowercase
    string2 = string2.lower()
    char_count = {}
    #Iterating through the string
    for char in string2:
        #Proceed only if the char is alphanumerical
        if char.isalnum():
            char_count[char] = char_count.get(char, 0) + 1

    #Calculating the most frequent character
    mostFrequentChar = max(char_count, key=char_count.get, default=None)

    #check for the most frequent character
    if char_count.get(mostFrequentChar, 0) > 1:
        return mostFrequentChar #return most frequent charater if present
    else:
        return None #return None if frequent character is not present


def fun3(string3):
    """This function takes string as an arguement and returns the tuple containing count of the
    number of letters, spaces and digits in the string"""
    #Initializing the counts
    letter_count = 0
    space_count = 0
    digit_count = 0

    # Iterating through characters in the given string
    for char in string3:
        if char.isalpha():  #Check if the character is an alphabet
            letter_count += 1 #increment letter_count by 1
        elif char.isspace():  #Check if the character is a space
            space_count += 1 #increment space_count by 1
        elif char.isdigit():  #Check if the character is a numeric
            digit_count += 1 #increment digit_count by 1

    # return the letter, space and digit count in a string
    return letter_count, space_count,digit_count
