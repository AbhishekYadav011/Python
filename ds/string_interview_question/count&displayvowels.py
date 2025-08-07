def check_vow(string, vowels):
    string = string.casefold()
    # Forms a dictionary with key as a vowel
    # and the value as 0
    count = {}.fromkeys(vowels, 0)
    for character in string:
        if character in vowels:
            count[character] += 1
    return count


string = "abhishek"
vowels = "aeiou"
print(check_vow(string, vowels))
