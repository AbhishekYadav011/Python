"""Write a python code to find the frequency of each word in a given string.
Input :  str[] = "Apple Mango Orange Mango Guava Guava Mango"
Output : frequency of Apple is : 1
         frequency of Mango is : 3
         frequency of Orange is : 1
         frequency of Guava is : 2
"""


def frequency(str1):
    listofword = str1.split()
    # used SET to remove duplicates in the listofword and get the unique word,every unique word will be pass
    # to count function
    uniqueword = set(listofword)
    for word in uniqueword:
        print("frequency of", word, "is :", listofword.count(word))

"""Adding extra function to see the all count in one dictionary"""

def check_vow(string, vowels):
    string = string.casefold()
    # Forms a dictionary with key as a vowel
    # and the value as 0
    count = {}.fromkeys(vowels, 0)
    for character in string:
        if character in vowels:
            count[character] += 1
    return count


if __name__ == '__main__':
    frequency("Apple Mango Orange Mango Guava Guava Mango")
