def palindrome_check(string:str)->None:
    string=string.casefold()
    string1=string
    print(string)
    print(string1.lower())
    rev_string=reversed(string)
    if string == rev_string:
        print('Palindrome')
    else:
        print('Not a Palindrome')

palindrome_check('rag%')