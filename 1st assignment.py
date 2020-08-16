import string

def pangram(string,alphabets):

    for char in alphabets:

        if char not in string.lower():

            return False

    return True

alphabets=string.ascii_lowercase

example="The Quick Brown Fox Jumps Over The Lazy Dog"

if (pangram(example,alphabets)==True):
    
    print("The given example is a pangram")

else:

    print("The given example is not a pangram")
