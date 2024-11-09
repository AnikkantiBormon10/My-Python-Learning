d ={} #empty dictionary
print(d)
mark = {

    "Out of": 100,
    "Anik" : 90,
    "pulok" : 92,
    "himel" :89,

}

print(mark)
print(mark.items())
print(mark.keys())
print(mark.values())
print(mark["Anik"])
mark.update({"Anik": 95 , "Akshor": 33})
print(mark)
print(mark.get("Anik1"))# if call wrong key then print 'none'
print(mark["Anik1"]) # if call wrong key then it returns an 'Error'



