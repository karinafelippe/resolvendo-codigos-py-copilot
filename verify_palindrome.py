word = input("Input word: ")

if word == word[::-1]:
    print("It is a palindrome!")
else:
    print("It is NOT a palindrome.")