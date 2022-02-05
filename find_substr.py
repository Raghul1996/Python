def find_substring(sentence:str,word:str)->None:
    index_string=sentence.find(word)
    print(f'Index of {word} in {sentence} is {index_string}')

find_substring('Raghul is a gud working guy','R')