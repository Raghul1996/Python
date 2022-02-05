def reverse_sentence_without_string_reversal(sentence:str) -> None:
    sentence_li=sentence.split(" ")
    li_reverse=sentence_li[::-1]
    li_new_reversed_list=[]
    for words in li_reverse:
        li_new_reversed_list.append(words)
    print(" ".join(li_reverse))

reverse_sentence_without_string_reversal("raghul is a good boy ")
    
    #input
    #raghul is a gud boy
    #output
    #boy good a is raghul