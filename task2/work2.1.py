__author__ = 'Administrator'

def countlist(list):
    mydict=dict()
    for x in list:
        a=x[0]
        mydict[a]=0
    #print mydict
    for x in list:
        i=0
        mydict[x[i]]=mydict[x[i]]+int(x[i+1])  #the key is x[i] is key ,x[i+1] is number
    print mydict
    return mydict
list=[['A','3'],['B','2'], ['C','3'], ['A','4'], ['B','5'], ['C','6'], ['A','1'], ['B','1'], ['C','1']]
countlist(list)