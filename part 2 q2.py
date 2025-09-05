# task 3
gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Tlevision", 1000,True, False, "Laptop Case", "Camera Lens"]
list_s=[]
listn=[]
listb=[]
for item in gadgets :
    if type(item) == str :
           list_s.append(item)
    elif type(item) == bool :
        listb.append(item)
    else :
        listn.append(item)

print(list_s)
print(listn)
print(listb)
