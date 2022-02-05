# def reverse_strings(sentence:str):
#     li_sentence=sentence.split(" ")
#     li_reverse=[]
#     for words in li_sentence:
#         li_reverse.append(words[::-1])
#     print(" ".join(li_reverse))

# reverse_strings("raghul is a gud boy")

def reverse_strings(sentence:str)->None:
    print(sentence[::-1])

reverse_strings("raghul is a gud boy")

#input
#raghul is a gud boy
#output
#yob dug a si luhgar

