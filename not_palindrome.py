def not_palindrome(sentence:str):
    li_not_palindrome=[]
    li_sentence=sentence.split(" ")
    for words in li_sentence:
        if words != words[::-1]:
            li_not_palindrome.append(words)
    print(" ".join(li_not_palindrome))

not_palindrome("Raghul is madam boy")