post = input("Write a post : ")
name = input("Enter the name for cheak which about post : ")
if(name.lower() in post.lower()):
    print( " post is about ", name)
else:
    print("post is not about", name)