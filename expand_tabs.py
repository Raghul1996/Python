def expand_tabs_string(string:str)->None:
    print(string)
    print('\t')
    print(string.expandtabs(12))
    print('\t')
    print(string)
expand_tabs_string('Raghul             is a gud working guy')
