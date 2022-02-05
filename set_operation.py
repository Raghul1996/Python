
def set_operation():
    seta = ['apple', 'orange', 'grapes', 'mango', 'starfruit']
    setb = ['papaya', 'mango', 'jackfruit', 'grapes', 'lychee'] 
    #print(union_set)
    intersection_set=list(set(seta)&set(setb))
    #print(intersection_set)
    diff_seta=list(set(seta)-set(setb))
    #print(diff_seta)
    diff_setb=list(set(setb)-set(seta))
    #print(diff_setb)
    diff_seta_setb=(list(set(seta)-set(setb)))+(list(set(set(setb)-set(seta))))
    #print(diff_seta_setb)
    seta_frozenset=frozenset(seta)
    #print(seta_frozenset)
    union_set=seta+diff_setb
    return(union_set,intersection_set,diff_seta,diff_setb,diff_seta_setb,seta_frozenset)
li=set_operation()
print(li)