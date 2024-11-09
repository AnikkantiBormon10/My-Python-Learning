comment = input("Enter the comment : ")
a='Make a lot of money'
b='buy now'
c='subscribe this'
d='click this'

if( comment == a or comment == b or comment == c or comment == d):
    print("spam comment")
else:
    print("Real comment")


# this is also currect :

# if( comment in a or comment in b or comment in c or comment in d):
#     print("spam comment")
# else:
#     print("Real comment")