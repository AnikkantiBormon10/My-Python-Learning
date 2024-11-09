
def list(l ,word):
    n=[]
    for i in l:
        if(not(i in word)):
            n.append(i.strip(word))
    return n


l= ["anik","himel","akhor","protay","h"]
word=input( "enter the word : ")
print(list(l,word))