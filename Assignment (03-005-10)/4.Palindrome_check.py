# palindrome check
def is_palindrome(word):
    word=word.lower()
    check_word=""
    for n in word:
        if n.isalnum:   # To check alphanumeric
            check_word+=n

    if check_word == check_word[::-1]:
        return True
    else:
        return False
Inp= input("Enter a word: ")
result= is_palindrome(Inp)
print(result)