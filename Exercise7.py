def CheckIsVowel(letter):
    vowelTurle = {'a','e','i','o','u','A','E','I','O','U','y','Y'}
    if letter in vowelTurle:
        print("This letter is vowel")
        return True
    else:
        print("This letter is not vowel")
        return False