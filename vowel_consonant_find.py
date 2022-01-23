def find_vowel_consonant():
    li_consonant=[]
    li_vowel=[]
    vowel,consonant=0,0
    sentence1=input('Enter the sentence')
    sentence1=sentence1.replace(" ","")
    for i in sentence1:
        if i not in 'aeiouAEIOU':
            li_consonant.append(i)
            consonant+=1
        else:
            li_vowel.append(i)
            vowel+=1
    print(f'Consonants in the given sentence are{li_consonant} and count is {consonant}')
    print(f'Vowels in the given sentence are {li_vowel} and count is {vowel}')

find_vowel_consonant()
    
        