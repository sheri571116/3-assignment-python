Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]
st=[]
n=[]

for item in Gadgets :
    if type(item) == str:
        
        st.append(item)
    else:
        n.append(item)

print(st)
print(n)

st.sort()
print(st)

st.sort(reverse=True)
print(st)

st.sort(key=len)
print(st)


n.sort()
print(n)

n.sort(reverse=True)
print(n)
    
